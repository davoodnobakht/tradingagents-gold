"""Test OpenRouter credentials without exposing the key or making a trade."""
import json, os, urllib.request, urllib.error
key = os.getenv("OPENROUTER_API_KEY")
if not key:
    raise SystemExit("OPENROUTER_API_KEY not configured. Add it to GitHub Codespaces secrets.")
req = urllib.request.Request("https://openrouter.ai/api/v1/key", headers={"Authorization": "Bearer " + key})
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        payload = json.load(r)
    data = payload.get("data", {})
    print("OpenRouter authentication: OK")
    print("Free model allowance:", data.get("free_model_daily_requests", "not reported"))
except urllib.error.HTTPError as e:
    print("OpenRouter authentication failed; HTTP status:", e.code)
    raise SystemExit(1)
