# Trading Bot Project - Living Context

**Last Updated:** April 12, 2026  
**Status:** Foundation complete → Conservative Silo strategy + basic simulation implemented. Tests & CI coming next.

## Project Overview
A modular multi-silo paper trading bot. Each silo has its own personality and risk rules. All funding flows through a central **General Account**. Currently focused on simulation only (no real money or live brokers).

### Core Philosophy
- Four distinct silos with different strategies
- Conservative Silo acts as a responsible fiduciary (capital preservation first)
- Profits can flow back to General Account
- Everything stays in paper-trading / simulation mode

## Current Silos

| Silo              | Personality            | Status       | Strategy                        |
|-------------------|------------------------|--------------|---------------------------------|
| **Conservative**  | Fiduciary (cautious)   | Active       | 50/200 SMA + strict risk rules  |
| Metals            | Defensive              | Planned      | TBD                             |
| Tech/Innovation   | Growth-oriented        | Planned      | TBD                             |
| Crypto            | Aggressive Sniper      | Planned      | TBD                             |

## Project Structure

```bash
trading_bot_project/
├── src/                          # All source code (src layout - best practice)
│   └── trading_bot/
│       ├── __init__.py
│       ├── main.py               # Entry point + simulation loop
│       └── ...                   # (will expand with core/, utils/, etc.)
├── accounts/
│   └── general_account.py        # Persistent funding source
├── strategies/
│   └── conservative.py           # 50/200 SMA + fiduciary risk controls
├── tests/                        # Unit tests (being added now)
│   └── test_conservative_silo.py
├── config/                       # Configuration files (future use)
├── data/                         # Persistent data (general_account.json, etc.)
├── logs/                         # Log files (future)
├── .github/
│   └── workflows/                # GitHub Actions CI (coming next)
├── 
├── pyproject.toml                # Poetry dependencies
├── poetry.lock
├── poetry.toml
├── setup.sh                      # Environment activation
├── PROJECT_CONTEXT.md            # ← This living document (single source of truth)
├── README.md
└── ...                           # (other root files)