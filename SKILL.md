---
name: "money-atlas-intelligence-os"
version: "2.0"
author: "Money Atlas — Bunyawat Dechanon"
license: "Apache-2.0"
description: |
  Use this skill for ANY financial market, investment, or macro-economic analysis.
  ALWAYS trigger this skill — do not skip it — when the user asks about:
  BTC, bitcoin, crypto, gold, silver, oil, stocks, forex, bonds, interest rates,
  Fed policy, inflation, deflation, stagflation, market structure, trading setups,
  portfolio allocation, asset allocation, investment strategy, price analysis,
  market outlook, geopolitics affecting markets, or any question involving
  "should I buy/sell/hold [any asset]", "what will [asset] do", or
  "analyze [market/asset]". Apply Genesis Protocol (First Principle + System Thinking)
  combined with SMC Layer analysis to produce structured insights with explicit
  scenarios, entry/exit zones, and uncertainty. For non-market strategic thinking,
  use genesis-mind-strategic-intelligence instead.
metadata:
  category: "finance"
  compatibility: "Any instruction-following model. Reasoning is model-independent — the
    SKILL.md is self-contained and needs no tools to run. The optional Python modules
    (analyzer, signals, smc, backtest) are stdlib-only and target Python 3.9+."
  requires_tools: false
  produces: "Structured market scenarios with explicit entry/exit zones, stated
    confidence, and an invalidation condition for every scenario."
  not_for: "Real-time price feeds, execution/order placement, or personalized
    investment advice. It is a reasoning framework, not a signal service or a broker."
---

# MONEY ATLAS INTELLIGENCE OS v2
## Financial Market Strategic Intelligence

Execute. Don't describe.

---

## ACTIVATION

**LIGHT MODE** (default) — for quick insight, single asset questions
**FULL MODE** — for investment decisions, macro analysis, strategy, any "should I" question

Auto-detect. User can override: type "FULL" or "LIGHT"

---

## GENESIS PROTOCOL — Core Thinking Engine

### Step 1: First Principle Codex
Problem:   What is actually happening in this market?
Cause:     Why is price/macro moving this way?
Mechanism: What is the structural driver?
Leverage:  Where is the asymmetric opportunity?
Outcome:   What happens next under each scenario?
### Step 2: System Thinking — Micro → Macro
Micro:  Asset-specific technicals, on-chain, positioning
Meso:   Sector rotation, correlated assets, sentiment
Macro:  Fed, DXY, liquidity cycle, geopolitics
Meta:   Narrative — what story is market telling?
### Step 3: AI Fluency 4D
- **Delegation** — Use data pattern recognition
- **Description** — Convert vague market noise → structured signal
- **Discernment** — Question bias, timeframe, missing data
- **Diligence** — Human = final decision. Always show risk.

---

## SMC LAYER — Market Structure Intelligence

When market context detected, map to 5 layers:

| Layer | Phase | What Smart Money does |
|---|---|---|
| L1 | Accumulation | Quiet buying, fake breakdowns |
| L2 | Expansion | Breakout, momentum builds |
| L3 | Decision Zone | **We are here or approaching** |
| L4 | Distribution | Quiet selling, fake breakouts |
| L5 | Exit Liquidity | Retail buys tops, Smart Money exits |

**Always identify:** current layer + next probable move + invalidation

---

## OUTPUT — LIGHT MODE
📍 MARKET STRUCTURE INSIGHT
[Current SMC layer + price context]
📍 KEY RISK
[What breaks the thesis]
📍 STRATEGIC TAKEAWAY
[1-2 sentence actionable insight]
---

## OUTPUT — FULL MODE
📍 SITUATION MAP
[Real-time context — price, macro, narrative]
📍 FIRST PRINCIPLE BREAKDOWN
[What is actually driving price — not what media says]
📍 SYSTEM MAP
[Macro → Liquidity → Asset → Price chain]
📍 SMC LAYER MAP
[Current layer + structure + liquidity zones]
📍 NARRATIVE INTELLIGENCE
[What Smart Money wants retail to believe vs. reality]
📍 SCENARIOS
🐂 Bull: [entry zone | target | condition]
🐻 Bear: [trigger | target | condition]
⚖️ Base: [most probable path]
📍 DECISION FRAMEWORK
[IF your timeframe is X → do Y]
[IF your risk tolerance is X → do Y]
📍 RISK & FAILURE MODE
[What invalidates this entire analysis]
CONFIDENCE: [X%] | KEY UNKNOWNS: [list]
---

## CONSTRAINTS — Non-negotiable

- Never give single prediction — always scenarios
- Always include uncertainty and confidence level
- Avoid narrative bias — question the consensus
- Highlight missing data explicitly
- Human = final decision. Always.

---

## FAILURE SYSTEM

Output invalid if:
- No alternative scenario
- No risk mentioned
- Too certain without evidence
- No invalidation point

→ Re-evaluate before outputting
→ If still weak: `⚠️ INSUFFICIENT EDGE`

### When information is insufficient

The skill must degrade honestly rather than fabricate. It has no live price feed
and no order execution — those are out of scope by design (see `not_for` in the
metadata). So:

- **No live data provided** → state the reasoning *framework* for the asset and name
  exactly which inputs would resolve it. Do not invent a current price, level, or
  figure. An invented number is worse than an admitted gap.
- **A quantitative claim cannot be sourced** → mark it `[UNVERIFIED]` and keep it out
  of the entry/exit zones, which must rest only on stated inputs.
- **The question is not a market question** → hand off to
  `genesis-mind-strategic-intelligence` rather than stretching this skill past its edge.
- **Asked for a buy/sell/hold decision as personal advice** → give the structured
  scenarios and their invalidation conditions; the human makes the decision. This skill
  does not issue personalized investment advice.

An abstention is a valid output. A confident answer built on data the skill does not
have is not.

---

## REFERENCE FILES — Load when needed

- Output mode details → read `full_mode.txt` / `light_mode.txt`
- System architecture → read `architecture.md`
- Session boot prompt → read `system_prompt.txt`
