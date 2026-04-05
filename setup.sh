#!/bin/bash
# setup.sh - Trading Bot Environment Setup

echo "🔧 Setting up Trading Bot environment with Poetry..."

# Ensure correct configuration
poetry config virtualenvs.in-project true --local

# Install dependencies if needed
poetry install --no-root

# Activate the environment
source .venv/bin/activate

echo "✅ Trading Bot environment is ready!"
echo "Python: $(python --version)"
echo "Pandas: $(python -c 'import pandas; print(pandas.__version__)' 2>/dev/null || echo 'Not found')"

echo ""
echo "=== Quick Commands ==="
echo "   ./setup.sh          # Full setup + activate"
echo "   source .venv/bin/activate   # Activate only"
echo "   tb                  # Quick alias to activate (type 'tb' in any terminal)"

# Add quick alias 'tb' to your shell
echo 'alias tb="source ~/Projects/trading_bot/.venv/bin/activate"' >> ~/.zshrc 2>/dev/null || true

echo ""
echo "✅ Alias 'tb' added. In any new terminal, just type 'tb' to activate the environment."
