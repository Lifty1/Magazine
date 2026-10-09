"""Independent fact-check of each article by a second model via OpenRouter.
Output: research/factcheck/<article>.md. Flagged items are then verified by hand."""
import json, os, sys, urllib.request, concurrent.futures as cf
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MODEL = sys.argv[1] if len(sys.argv) > 1 else 'openai/gpt-5.1'
PROMPT = """You are a meticulous magazine fact-checker. Below is an article from a natural-history magazine (written October 2026).
List every factual claim you believe is WRONG, DOUBTFUL, or OVERSTATED (dates, numbers, names, places, quotes, attributions, causal claims).
For each: quote the claim, say what you believe is correct, and give your confidence (high/medium/low). Ignore style. Do not list claims you believe are correct.
If you know nothing contradicting a claim, do not list it. Be concise.

ARTICLE:
"""
def check(name):
    if os.path.exists(os.path.join(ROOT, 'research', 'factcheck', name)): return name, -1
    text = open(os.path.join(ROOT, 'content', name), encoding='utf8').read()
    body = json.dumps({'model': MODEL, 'max_tokens': 3000, 'reasoning': {'effort': 'low'}, 'messages': [{'role': 'user', 'content': PROMPT + text}]}).encode()
    req = urllib.request.Request('https://openrouter.ai/api/v1/chat/completions', data=body, headers={'Content-Type': 'application/json'})
    r = json.load(urllib.request.urlopen(req, timeout=600))
    out = r['choices'][0]['message']['content'] or ''
    if not out: return name, 0
    open(os.path.join(ROOT, 'research', 'factcheck', name), 'w', encoding='utf8').write(f'# Fact-check of {name} by {MODEL}\n\n{out}\n')
    return name, len(out)
names = sorted(f for f in os.listdir(os.path.join(ROOT, 'content')) if f.endswith('.md'))
with cf.ThreadPoolExecutor(1) as ex:
    for n, l in ex.map(check, names): print(n, l)
