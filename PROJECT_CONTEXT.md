# Trading Bot Project - Living Context

**Last Updated:** April 5, 2026  
**Status:** Foundation complete → Ready for strategy development

## Current Setup
- **Python**: 3.14.3 via pyenv + Poetry
- **Environment activation**: `tb` or `./setup.sh`
- **Run the bot**: `runbot` (after activation)
- **Project structure**:
  - `src/trading_bot/main.py` → entry point
  - `src/trading_bot/` → main package
  - `config/`, `strategies/`, `tests/`, `data/`, `logs/`
- **Workflow**:
  1. Open terminal → `cd ~/Projects/trading_bot`
  2. `tb` (or `./setup.sh`)
  3. `runbot` to test

## Next Phase
We are ready to implement the actual trading logic.

## Trading Bot Goals (Please fill in / update)
- **Market**: ? (Crypto spot/futures, Stocks, etc.)
- **Strategy type**: ? (Moving average crossover, RSI, custom idea, etc.)
- **Timeframe**: ? (1m, 5m, hourly, daily...)
- **Development order**: Backtesting first or live/paper trading?
- **Exchange/Broker**: ? (Binance, Bybit, Alpaca, etc.)
- **Other requirements**: Risk management, position sizing, logging, etc.

## Important Notes
- Always activate with `tb` before running code
- Never commit `.env`, `.venv`, or sensitive keys
- Use `PROJECT_CONTEXT.md` to keep me updated in new sessions

