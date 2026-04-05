# Trading Bot Project Context

**Last Updated:** 2026-04-05  
**Status:** Foundation + basic structure complete

## Current Tech Stack
- Python 3.14.3 (via pyenv)
- Poetry for dependency management
- Project layout:
  - `src/trading_bot/` → main package
  - `config/` → configuration
  - `strategies/` → trading strategies
  - `tests/` → tests
  - `data/`, `logs/` → data and logs
- Activation: Use `tb` alias or `./setup.sh`
- Run bot: `runbot` alias (after `tb`)

## Current Files
- `setup.sh` — setup + activation
- `src/trading_bot/main.py` — basic entry point
- `pyproject.toml` — dependencies
- `.vscode/settings.json` — VS Code config

## Goals / Next Phase
We are ready to implement the actual trading logic.

## User Preferences (update as needed)
- IDE: VS Code (with `tb` alias for activation)
- Keep using Poetry for now
- Console + VS Code workflow

## Trading Bot Requirements (to be filled)
- Market: 
- Strategy type: 
- Timeframe: 
- Backtesting vs Live: 
- Exchange/Broker: 

## Important Notes
- Always activate environment with `tb` before running code
- Use `python -m src.trading_bot.main` or `runbot` to start the bot
- Never commit `.env`, logs, or `.venv`

---

**How to use this file:**
When starting a new session, paste the content of `PROJECT_CONTEXT.md` at the top of your message so I have full context.

