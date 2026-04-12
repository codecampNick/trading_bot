#!/bin/bash
# setup.sh - Trading Bot Environment Setup

echo "🔧 Setting up Trading Bot environment with Poetry..."

# Ensure correct configuration
poetry config virtualenvs.in-project true --local

# Install dependencies
poetry install --no-root

# Activate the environment
source .venv/bin/activate

echo "✅ Trading Bot environment is ready!"
echo "Python: $(python --version)"

echo ""
echo "=== Quick Commands ==="
echo "   tb       → Activate environment"
echo "   runbot   → Run the trading bot"
echo "   ./setup.sh → Full setup"

# Update aliases to use the correct path (src/core)
echo 'alias tb="source ~/Projects/trading_bot/.venv/bin/activate"' >> ~/.zshrc 2>/dev/null || true
echo 'alias runbot="python src/core/main.py"' >> ~/.zshrc 2>/dev/null || true

echo "✅ Aliases updated. Type 'tb' then 'runbot' to run."
