"""Standalone gold signal research; not a validated backtest and never places orders."""
import argparse, csv, datetime, pathlib
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", default="GC=F")
    p.add_argument("--start", default="2026-01-01")
    p.add_argument("--end", default="2026-01-31")
    p.add_argument("--every", type=int, default=7)
    p.add_argument("--provider", default="openai")
    p.add_argument("--quick-model")
    p.add_argument("--deep-model")
    p.add_argument("--confirm-historical-data", action="store_true")
    a = p.parse_args()
    if not a.confirm_historical_data:
        p.error("Verify point-in-time historical market/news availability first; then explicitly acknowledge.")
    if a.every < 1:
        p.error("--every must be positive")
    start, end = datetime.date.fromisoformat(a.start), datetime.date.fromisoformat(a.end)
    if start > end:
        p.error("start must not exceed end")
    config = DEFAULT_CONFIG.copy()
    config["llm_provider"] = a.provider
    if a.quick_model:
        config["quick_think_llm"] = a.quick_model
    if a.deep_model:
        config["deep_think_llm"] = a.deep_model
    graph = TradingAgentsGraph(["market", "news"], config=config, debug=False)
    pathlib.Path("results").mkdir(exist_ok=True)
    with open("results/gold_decisions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "ticker", "decision", "status"])
        w.writeheader()
        d = start
        while d <= end:
            try:
                _, decision = graph.propagate(a.ticker, d.isoformat())
                w.writerow(dict(date=d.isoformat(), ticker=a.ticker, decision=str(decision), status="ok"))
                f.flush()
                print(d, decision)
            except Exception as exc:
                w.writerow(dict(date=d.isoformat(), ticker=a.ticker, decision="", status=f"error: {exc}"))
                f.flush()
                raise
            d += datetime.timedelta(days=a.every)
    print("Decisions saved; no P&L calculated or validated.")

if __name__ == "__main__":
    main()
