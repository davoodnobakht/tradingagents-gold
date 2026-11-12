"""Inspect upstream API signatures; does not prove backtest validity."""
import importlib, inspect, json, pathlib
out = {}
for name in ["tradingagents.graph.trading_graph", "tradingagents.default_config", "tradingagents.backtest"]:
    try:
        mod = importlib.import_module(name)
        item = {"found": True}
        if hasattr(mod, "TradingAgentsGraph"):
            cls = mod.TradingAgentsGraph
            item["init_signature"] = str(inspect.signature(cls))
            if hasattr(cls, "propagate"):
                item["propagate_signature"] = str(inspect.signature(cls.propagate))
        out[name] = item
    except Exception as e:
        out[name] = {"found": False, "error": str(e)}
pathlib.Path("results").mkdir(exist_ok=True)
pathlib.Path("results/upstream_api.json").write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
