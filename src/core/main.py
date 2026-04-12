"""
Trading Bot Main Entry Point
"""

from datetime import datetime
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.strategies.conservative import ConservativeStrategy

def main():
    print("=" * 70)
    print("🚀 Trading Bot - Conservative Silo (Fiduciary Mode)")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    conservative = ConservativeStrategy(initial_capital=100_000.0)

    print(f"\nInitial Capital: ${conservative.capital:,.2f}")
    print("Strategy: 50/200 SMA crossover")
    print("-" * 50)

    status = conservative.get_status()
    print(f"\nStatus:")
    print(f"  Cash: ${status['cash_balance']:,.2f}")
    print(f"  Open Positions: {status['open_positions']}")

    print("\n✅ Conservative Silo loaded.")
    print("=" * 70)

if __name__ == "__main__":
    main()
