# Trading Bot Project - Living Context

**Last Updated:** April 12, 2026  
**Status:** Foundation complete → Starting Conservative Silo development

## Current Setup
- Python 3.14.3 + Poetry
- Activation: `tb` or `./setup.sh`
- Run bot: `runbot`
- Project structure: `src/trading_bot/`, `config/`, `strategies/`, `tests/`, `data/`, `logs/`

## Silo Strategy (4 Silos)
1. **Conservative Silo** ← **We are building this first**
2. Metals Silo
3. Tech/Innovation Silo
4. Crypto Silo (aggressive sniper)

**Overall Philosophy**:
- Each silo has its own rules and personality
- All silos are funded from a **General Account** (simple cash balance for now)
- Profits from any silo → portion returned to General Account
- No real money used → Paper trading / simulation only

## Current Decisions
- **Starting Silo**: Conservative (steady, reliable growth)
- **Conservative Silo Personality**: Acts like a **fiduciary** — cautious, responsible, prioritizes capital preservation with modest but consistent returns
- **Trading Mode**: Paper trading (simulated trades only)
- **General Account**: Simple cash balance in code (no broker connection yet)
- **Development Order**: Build Conservative Silo first, then expand to others

## Next Steps
- Design Conservative Silo strategy (50/200 SMA crossover with strict risk controls)
- Implement General Account funding logic
- Create backtesting/paper trading framework
- Build modular architecture so other silos can be added easily

## Important Notes
- Always activate with `tb`
- Never commit real API keys or money
- Use this file to keep context across sessions

