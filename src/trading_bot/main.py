"""
Trading Bot Main Entry Point
Conservative Silo (Fiduciary Mode) with General Account funding
"""

import sys
from datetime import datetime
from trading_bot.accounts.general_account import GeneralAccount
from trading_bot.strategies.conservative import ConservativeStrategy

def run():
    print("=" * 70)
    print("🚀 Trading Bot - Conservative Silo (Fiduciary Mode)")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # Initialize General Account (persistent)
    general_account = GeneralAccount()

    # Initialize Conservative Silo
    conservative_silo = ConservativeStrategy(general_account)

    print("\n📊 Paper Trading Simulation Mode")
    print("No real market data connected yet.\n")

    # Show initial status
    print("Current Status:")
    ga_status = general_account.get_status()
    silo_status = conservative_silo.get_status()
    
    print(f"  General Account Balance : ${ga_status['general_balance']:.2f}")
    print(f"  Conservative Silo       : ${silo_status['cash_balance']:.2f} "
          f"({silo_status['open_positions']} open positions)")
    print(f"  Total Trades            : {silo_status['total_trades']}")

    print("\n✅ Conservative Silo is loaded and ready.")
    print("=" * 70)

    # TODO: Later we will add a simulation loop with fake or real data here

if __name__ == "__main__":
    run()