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
echo "   tb                  # Activate environment"
echo "   runbot              # Run the trading bot"
echo ""
echo "Project Context: See PROJECT_CONTEXT.md"
