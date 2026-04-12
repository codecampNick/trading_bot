"""
Trading Bot Main Entry Point
"""

from datetime import datetime
import sys
from pathlib import Path

# Add src to Python path so 'trading_bot' package can be found
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.trading_bot.strategies.conservative import ConservativeStrategy

def main():
    print("=" * 70)
    print("🚀 Trading Bot - Conservative Silo (Fiduciary Mode)")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    conservative = ConservativeStrategy(initial_capital=100.0)

    print(f"\nInitial Capital: ${conservative.capital:,.2f}")
    print("Strategy: 50/200 SMA crossover with strict risk controls")
    print("-" * 50)

    print("\n📊 Paper Trading Simulation Mode")
    print("No real market data connected yet.")

    status = conservative.get_status()
    print(f"\nCurrent Status:")
    print(f"  Cash Balance   : ${status['cash_balance']:,.2f}")
    print(f"  Open Positions : {status['open_positions']}")
    print(f"  Total Trades   : {status['total_trades']}")

    print("\n✅ Conservative Silo is loaded and ready.")
    print("=" * 70)

if __name__ == "__main__":
    main()
