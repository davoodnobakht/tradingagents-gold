#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip
if [ ! -d upstream/TradingAgents ]; then git clone https://github.com/TauricResearch/TradingAgents.git upstream/TradingAgents; fi
python -m pip install -e upstream/TradingAgents
python verify_upstream.py
