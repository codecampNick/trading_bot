# Trading Bot Project - Living Context

**Last Updated:** April 18, 2026  
**Status:** Foundation complete → Conservative Silo running successfully via Poetry

## Project Overview
A modular multi-silo paper trading bot. Each silo has its own personality and risk rules. All funding flows through a central **General Account**. Currently focused on simulation / paper trading only (no real money or live brokers connected yet).

### Core Philosophy
- Four distinct silos with different risk personalities
- Conservative Silo acts as a responsible fiduciary (capital preservation first)
- Profits can flow back to the General Account
- Everything remains in paper-trading / simulation mode for now

## Current Silos

| Silo              | Personality            | Status       | Strategy                        |
|-------------------|------------------------|--------------|---------------------------------|
| **Conservative**  | Fiduciary (cautious)   | Active       | 50/200 SMA + strict risk rules  |
| Metals            | Defensive              | Planned      | TBD                             |
| Tech/Innovation   | Growth-oriented        | Planned      | TBD                             |
| Crypto            | Aggressive Sniper      | Planned      | TBD                             |

## Project Structure (Current)

```bash
trading_bot_project/
├── src/
│   └── trading_bot/
│       ├── __init__.py
│       ├── main.py                    # Entry point + run() function
│       ├── accounts/
│       │   └── general_account.py     # Central funding account
│       ├── strategies/
│       │   └── conservative.py        # Conservative silo logic
│       └── ...
├── config/
├── data/
│   └── general_account.json           # Persistent account state
├── info/
│   └── set_up.md                      # Setup instructions
├── logs/
├── tests/
├── pyproject.toml                     # Poetry configuration
├── poetry.lock
├── PROJECT_CONTEXT.md                 # This living document
├── README.md
├── setup.sh
└── ...