#!/bin/bash
# setup.sh - Reproducible setup for the trading bot

echo "🔧 Setting up trading bot environment..."

# Ensure correct Python version with pyenv
pyenv install -s 3.14.3
pyenv local 3.14.3

# Create virtual environment
python -m venv .venv

# Activate and install dependencies
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup complete!"
echo "To start working:"
echo "   source .venv/bin/activate"
echo "   python -c \"import pandas; print('Ready to build trading bot!')\""
