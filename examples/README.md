# Examples

Two kinds of example live here:

- **Worked examples** (`worked/*.md`) — a real question and the *shape* of the
  answer the skill produces. These show an agent, or a person evaluating the
  skill, what "good output" looks like before installing it.
- **Runnable demo** (`full_system_demo.py`) — drives the optional Python engines
  end to end over sample OHLCV data.

## Worked examples

| File | Question | What it demonstrates |
|---|---|---|
| [worked/01-btc-light-mode.md](worked/01-btc-light-mode.md) | "Quick read on BTC?" | LIGHT mode: one scenario, confidence, invalidation |
| [worked/02-gold-full-mode.md](worked/02-gold-full-mode.md) | "Should I add gold here?" | FULL mode: First Principle → SMC → scenarios with entry/exit |
| [worked/03-insufficient-data.md](worked/03-insufficient-data.md) | "Where's BTC headed?" (no data) | Honest degradation — the skill abstains instead of inventing a price |

Every worked example ends with an **invalidation condition**, because an output
without one is invalid by the skill's own FAILURE SYSTEM.

## Running the demo

```bash
pip install -r ../requirements.txt   # if the engines need optional deps
python full_system_demo.py
```

The reasoning in `SKILL.md` needs none of this — it runs on the model alone. The
Python engines are an optional execution layer for when you want to drive the
same structure over real candles.
