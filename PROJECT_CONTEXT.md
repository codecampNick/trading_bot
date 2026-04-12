# Trading Bot Project - Living Context

**Last Updated:** April 12, 2026  
**Status:** Foundation complete → Conservative Silo strategy implemented + basic simulation running

## Project Overview
A modular, multi-silo trading bot focused on paper trading and simulation only.  
Each silo operates with its own personality, rules, and risk profile. All silos are funded from a central **General Account**.

### Core Philosophy
- **Four Silos** with distinct strategies and risk personalities
- Capital flows only from General Account → Silos (and back on profits)
- Strict capital preservation in Conservative Silo
- No real money or live broker connections yet
- Everything remains fully simulated / paper trading

## Current Silos

| Silo                | Personality          | Status                  | Strategy                          | Priority |
|---------------------|----------------------|-------------------------|-----------------------------------|----------|
| **Conservative**    | Fiduciary (cautious) | **Active**              | 50/200 SMA Crossover + strict risk | 1        |
| Metals              | Defensive            | Not started             | To be defined                     | 2        |
| Tech/Innovation     | Growth-oriented      | Not started             | To be defined                     | 3        |
| Crypto              | Aggressive Sniper    | Not started             | To be defined                     | 4        |

## Current Technical Setup
- **Language**: Python 3.14.3
- **Dependency Management**: Poetry
- **Activation**: `tb` or `./setup.sh`
- **Run Command**: `runbot`
- **Key Directories**:
  - `src/trading_bot/`
  - `accounts/`
  - `strategies/`
  - `data/`
  - `logs/`
  - `tests/`
  - `config/`

## Key Components Implemented

- **GeneralAccount** (`accounts/general_account.py`)
  - Persistent JSON storage (`data/general_account.json`)
  - 25% max allocation per silo (easily configurable)
  - Full funding history and audit trail

- **ConservativeStrategy** (`strategies/conservative.py`)
  - True 50/200 SMA Golden Cross strategy
  - Strict fiduciary risk controls:
    - Only long positions
    - Price must be above 200 SMA (trend filter)
    - 2% max risk per trade
    - 10% max position exposure
    - 5% hard stop-loss
    - 8% trailing stop
    - Risk-based position sizing

- **Simulation Engine**
  - Fake daily price data generator (realistic drift + volatility)
  - Daily simulation loop with signal generation and trade execution
  - Stop-loss and trailing stop monitoring
  - Realized P&L tracking

## Recent Changes (April 12, 2026)
- Upgraded `ConservativeStrategy` with proper SMA crossover logic and fiduciary risk rules
- Added basic paper trading simulation loop in `main.py`
- Improved status reporting and profit tracking
- Conservative Silo now actively simulates trades on fake SPY data

## Next Steps (Prioritized)

1. **Test & Tune Conservative Silo**
   - Run multiple simulations and analyze behavior
   - Tune risk parameters if needed (stop-loss, position sizing, etc.)
   - Add logging of all trades to file

2. **Improve Simulation Realism**
   - Replace fake data with real historical data (yfinance or Polygon)
   - Add proper backtesting framework
   - Support multiple symbols

3. **Architecture Improvements**
   - Create base `Silo` abstract class for better modularity
   - Move simulation logic into a dedicated `PaperTrader` or `Simulator` class
   - Add configuration system (`config/`)

4. **Future Silos**
   - Design Metals Silo strategy
   - Design Tech/Innovation Silo strategy

## Important Rules
- Always activate environment with `tb`
- Never commit real API keys or credentials
- All trading is **paper trading / simulation only**
- Use this file to maintain living context across sessions

## Development Guidelines
- Keep silos independent but share common utilities
- Prioritize clarity and safety over optimization
- All risk controls must be explicit and auditable
- Maintain separation between General Account and individual silos

---

**This document is the single source of truth for project direction.**
Update it after every major milestone.