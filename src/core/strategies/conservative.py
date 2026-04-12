"""
Conservative Silo Strategy - Fiduciary Style
Uses 50/200 SMA crossover with strict risk controls.
Prioritizes capital preservation with modest, reliable growth.
"""

import pandas as pd
from datetime import datetime
from typing import Dict, Optional

class ConservativeStrategy:
    def __init__(self, initial_capital: float = 100_000.0):
        self.name = "Conservative"
        self.capital = initial_capital
        self.positions: Dict[str, Dict] = {}  # symbol -> position details
        self.trade_history = []
        self.max_risk_per_trade = 0.02   # 2% max risk per trade
        self.max_portfolio_exposure = 0.10  # 10% max total exposure

    def generate_signal(self, df: pd.DataFrame, symbol: str) -> str:
        """Generate signal based on 50/200 SMA crossover."""
        if len(df) < 200:
            return "hold"

        # Calculate moving averages
        df = df.copy()
        df['sma50'] = df['close'].rolling(window=50).mean()
        df['sma200'] = df['close'].rolling(window=200).mean()

        latest = df.iloc[-1]

        if latest['sma50'] > latest['sma200'] and latest['sma50'] > latest['close'] * 0.98:
            return "buy"      # Golden Cross with confirmation
        elif latest['sma50'] < latest['sma200']:
            return "sell"     # Death Cross
        else:
            return "hold"

    def calculate_position_size(self, price: float) -> int:
        """Calculate conservative position size."""
        risk_amount = self.capital * self.max_risk_per_trade
        stop_loss_distance = price * 0.06  # assume 6% stop-loss
        shares = int(risk_amount / stop_loss_distance)
        return max(1, shares)  # at least 1 share

    def execute_paper_trade(self, symbol: str, signal: str, price: float, timestamp: datetime):
        """Simulate a paper trade for the silo."""
        if signal == "buy" and symbol not in self.positions:
            shares = self.calculate_position_size(price)
            cost = shares * price
            
            if cost <= self.capital * self.max_portfolio_exposure:
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
                    "price": price
                })
                print(f"[{timestamp.date()}] CONSERVATIVE BUY {shares} {symbol} @ ${price:.2f}")

        elif signal == "sell" and symbol in self.positions:
            position = self.positions.pop(symbol)
            proceeds = position["shares"] * price
            profit = proceeds - (position["shares"] * position["entry_price"])
            
            self.capital += proceeds
            self.trade_history.append({
                "time": timestamp,
                "symbol": symbol,
                "action": "SELL",
                "shares": position["shares"],
                "price": price,
                "profit": profit
            })
            print(f"[{timestamp.date()}] CONSERVATIVE SELL {position['shares']} {symbol} @ ${price:.2f} | Profit: ${profit:.2f}")

    def get_status(self) -> dict:
        """Return current status of the Conservative Silo."""
        total_exposure = sum(pos["shares"] * pos["entry_price"] for pos in self.positions.values())
        return {
            "silo": self.name,
            "cash_balance": round(self.capital, 2),
            "open_positions": len(self.positions),
            "total_exposure": round(total_exposure, 2),
            "total_trades": len(self.trade_history)
        }
