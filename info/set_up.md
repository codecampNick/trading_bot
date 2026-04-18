How to Run the Bot (Current)Development / LocalUse the alias: tb
(This cds into the project and runs poetry run runbot)
Direct command: poetry run runbot

Setup SummaryUses Poetry for dependency and environment management
Entry point defined in pyproject.toml under [project.scripts]
src/ layout with trading_bot as the main package
accounts/ and strategies/ are now properly inside the trading_bot package

Development          Workflowbashtree

tb                    # Start the bot (recommended)
poetry run runbot     # Direct run
poetry install        # Install / update dependencies
poetry check          # Validate configuration

