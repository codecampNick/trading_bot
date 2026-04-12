"""
Conservative Silo - Fiduciary Mode
Implements 50/200 SMA Crossover with strict risk controls.
Acts like a responsible fiduciary: capital preservation first, steady modest returns.
"""

import pandas as pd
from datetime import datetime
from typing import Dict, Optional, List
from accounts.general_account import GeneralAccount


class ConservativeStrategy:
    def __init__(self, general_account: GeneralAccount):
        self.name = "Conservative"
        self.general_account = general_account
        
        # Funding
        self.requested_funding = 25.0          # Initial ask (will be capped at 25% of General)
        self.funded_amount = 0.0
        self.capital = 0.0                     # Current cash + value of open positions
        
        # Positions & History
        self.positions: Dict[str, Dict] = {}   # symbol -> position details
        self.trade_history: List[Dict] = []
        
        # Fiduciary Risk Controls (Conservative)
        self.max_risk_per_trade = 0.02         # 2% of current capital at risk per trade
        self.max_position_size = 0.10          # Max 10% of capital in any single position
        self.stop_loss_pct = 0.05              # 5% hard stop-loss
        self.trailing_stop_pct = 0.08          # 8% trailing stop (once in profit)

        # Request initial funding from General Account
        self._request_funding()

    def _request_funding(self):
        """Request funding from General Account (respects 25% rule)."""
        allocated = self.general_account.allocate_to_silo(
            self.name, self.requested_funding
        )
        self.funded_amount = allocated
        self.capital = allocated
        print(f"✅ {self.name} Silo funded with ${allocated:.2f} from General Account")

    def generate_signal(self, df: pd.DataFrame, symbol: str) -> str:
        """
        Generate trading signal using 50/200 SMA crossover with strict fiduciary filters.
        Only long positions. Very conservative.
        """
        if len(df) < 200:
            return "hold"

        df = df.copy()
        
        # Calculate indicators
        df['sma50'] = df['close'].rolling(window=50).mean()
        df['sma200'] = df['close'].rolling(window=200).mean()
        
        latest = df.iloc[-1]
        prev = df.iloc[-2] if len(df) > 1 else latest

        # Strict trend filter: Only consider longs when price is above 200 SMA
        if latest['close'] <= latest['sma200']:
            return "hold"   # No trading against the long-term trend

        # Golden Cross / Buy Signal
        if (prev['sma50'] <= prev['sma200'] and 
            latest['sma50'] > latest['sma200'] and
            latest['close'] > latest['sma50']):   # Price confirming the crossover
            return "buy"

        # Death Cross / Sell Signal
        if (prev['sma50'] >= prev['sma200'] and 
            latest['sma50'] < latest['sma200']):
            return "sell"

        # Also sell if we breach stop-loss (will be checked in position management too)
        return "hold"

    def calculate_position_size(self, price: float) -> int:
        """Calculate shares based on risk (never risk more than 2% of capital)."""
        if self.capital <= 0 or price <= 0:
            return 0

        risk_amount = self.capital * self.max_risk_per_trade
        stop_loss_distance = price * self.stop_loss_pct
        
        if stop_loss_distance <= 0:
            return 0
            
        shares = int(risk_amount / stop_loss_distance)
        
        # Also respect max position size (10% of capital)
        max_shares_by_exposure = int((self.capital * self.max_position_size) / price)
        
        shares = min(shares, max_shares_by_exposure)
        return max(1, shares) if shares > 0 else 0

    def check_stop_loss(self, symbol: str, current_price: float, timestamp: datetime) -> bool:
        """Check if stop-loss or trailing stop is triggered."""
        if symbol not in self.positions:
            return False
            
        position = self.positions[symbol]
        entry_price = position["entry_price"]
        shares = position["shares"]
        
        # Hard stop-loss
        stop_price = entry_price * (1 - self.stop_loss_pct)
        
        if current_price <= stop_price:
            self._close_position(symbol, current_price, timestamp, reason="stop_loss")
            return True
        
        # Simple trailing stop (if in profit)
        if current_price > entry_price:
            trail_price = current_price * (1 - self.trailing_stop_pct)
            if current_price <= trail_price:   # This is simplified - can be improved later
                self._close_position(symbol, current_price, timestamp, reason="trailing_stop")
                return True
                
        return False

    def _close_position(self, symbol: str, price: float, timestamp: datetime, reason: str = "sell"):
        """Internal method to close a position."""
        if symbol not in self.positions:
            return
            
        position = self.positions.pop(symbol)
        proceeds = position["shares"] * price
        profit = proceeds - (position["shares"] * position["entry_price"])
        
        self.capital += proceeds
        
        self.trade_history.append({
            "time": timestamp,
            "symbol": symbol,
            "action": "SELL",
            "shares": position["shares"],
            "price": round(price, 2),
            "profit": round(profit, 2),
            "reason": reason
        })
        
        print(f"[{timestamp.date()}] SELL {position['shares']} {symbol} @ ${price:.2f} "
              f"| Profit: ${profit:.2f} | Reason: {reason}")

    def execute_paper_trade(self, symbol: str, signal: str, price: float, timestamp: datetime):
        """Execute buy or sell in paper trading mode."""
        # First check existing positions for stops
        if symbol in self.positions:
            self.check_stop_loss(symbol, price, timestamp)

        if signal == "buy" and symbol not in self.positions:
            shares = self.calculate_position_size(price)
            if shares == 0:
                return
                
            cost = shares * price
            if cost > self.capital * self.max_position_size:
                return  # Safety check

            self.positions[symbol] = {
                "shares": shares,
                "entry_price": price,
                "entry_time": timestamp
            }
            self.capital -= cost
            
            self.trade_history.append({
                "time": timestamp,
                "symbol": symbol,
                "action": "BUY",
                "shares": shares,
                "price": round(price, 2)
            })
            
            print(f"[{timestamp.date()}] BUY {shares} {symbol} @ ${price:.2f} | Cost: ${cost:.2f}")

        elif signal == "sell" and symbol in self.positions:
            self._close_position(symbol, price, timestamp, reason="signal")

    def get_status(self) -> dict:
        """Return current status of the silo."""
        total_exposure = sum(
            pos["shares"] * pos.get("entry_price", 0) 
            for pos in self.positions.values()
        )
        
        total_profit = sum(
            trade.get("profit", 0) 
            for trade in self.trade_history if trade.get("action") == "SELL"
        )
        
        return {
            "silo": self.name,
            "funded_amount": round(self.funded_amount, 2),
            "cash_balance": round(self.capital, 2),
            "open_positions": len(self.positions),
            "total_exposure": round(total_exposure, 2),
            "total_trades": len(self.trade_history),
            "realized_profit": round(total_profit, 2)
        }