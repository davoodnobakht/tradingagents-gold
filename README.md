# TradingAgents Gold — Standalone Research

Independent research wrapper for [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents). No connection to prior XAUUSD bots; no live trading.

## GitHub Codespaces
Open **Code → Codespaces → Create codespace on main**. The devcontainer runs `bash setup.sh` to install upstream TradingAgents. Inspect `results/upstream_api.json` for compatibility.

**Important:** The default research script refuses to run historical experiments until point-in-time market/news availability has been independently checked. Do not enable the flag without verification. Trading decisions alone are **not** a valid backtest or evidence of returns.

Run after configuring model credentials as Codespaces secrets (never commit tokens):

```bash
python run_gold.py --ticker 'GC=F' --start 2026-01-01 --end 2026-01-31 --every 7 --confirm-historical-data
```

The above flag is a manual acknowledgment, not an automated validation. API usage may incur charges.

See `README_FA.md` for Persian guidance.
