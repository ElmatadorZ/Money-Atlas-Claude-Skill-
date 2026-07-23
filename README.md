# Money Atlas Intelligence OS
### Claude Skill (Agent) — Financial Market Strategic Intelligence

**Version:** 2.0  
**Author:** Bunyawat Dechanon (ElmatadorZ)  
**Brand:** Money Atlas / Alternative Slowbar  
**Type:** Custom Skill (SKILL.md format)

---

## What This Is

A skill that transforms financial market questions into structured, scenario-based intelligence.

Not a prediction engine.  
Not a signal bot.  
A thinking system — built to reason the way a disciplined analyst does.

When you ask about BTC, gold, macro, forex, or any asset — this skill activates a multi-layer reasoning pipeline that separates what's actually happening from what the market narrative wants you to believe.

---

## Core Engine

### Genesis Protocol — 3-Step Thinking Pipeline

**Step 1: First Principle Codex**
Deconstruct the market from root causes — not price action alone.
- What is *actually* happening?
- Why is price/macro moving this way?
- What is the structural driver?
- Where is the asymmetric opportunity?
- What happens next under each scenario?

**Step 2: System Thinking — Micro → Macro**
- Micro: Asset-specific technicals, on-chain data, positioning
- Meso: Sector rotation, correlated assets, sentiment
- Macro: Fed, DXY, liquidity cycle, geopolitics
- Meta: What narrative is the market constructing — and who benefits?

**Step 3: AI Fluency 4D**
- Delegation — Pattern recognition across data
- Description — Convert market noise → structured signal
- Discernment — Question bias, timeframe, missing information
- Diligence — Human makes the final decision. Always.

---

### SMC Layer — Smart Money Cycle Map

Identifies where price is in the institutional cycle:

| Layer | Phase | What's Happening |
|---|---|---|
| L1 | Accumulation | Quiet buying, engineered fake breakdowns |
| L2 | Expansion | Breakout, momentum building |
| L3 | Decision Zone | High-stakes inflection point |
| L4 | Distribution | Quiet selling, engineered fake breakouts |
| L5 | Exit Liquidity | Retail buys tops, institutions exit |

Every analysis maps the current layer + next probable move + invalidation condition.

---

## Output Modes

### LIGHT MODE — Quick Insight
For single-asset questions and fast reads.

```
📍 MARKET STRUCTURE INSIGHT
[SMC layer + price context]

📍 KEY RISK
[What breaks the thesis]

📍 STRATEGIC TAKEAWAY
[1-2 sentence actionable insight]
```

### FULL MODE — Deep Analysis
For investment decisions, macro analysis, strategy, or "should I" questions.

```
📍 SITUATION MAP
📍 FIRST PRINCIPLE BREAKDOWN
📍 SYSTEM MAP (Macro → Liquidity → Asset → Price)
📍 SMC LAYER MAP
📍 NARRATIVE INTELLIGENCE
📍 SCENARIOS
   🐂 Bull: [entry zone | target | condition]
   🐻 Bear: [trigger | target | condition]
   ⚖️ Base: [most probable path]
📍 DECISION FRAMEWORK
📍 RISK & FAILURE MODE
   CONFIDENCE: [X%] | KEY UNKNOWNS: [list]
```

Mode is auto-detected from question context.  
User can override: type `FULL` or `LIGHT` at any time.

---

## Trigger Topics

This skill activates when you ask about:

- **Crypto:** BTC, ETH, altcoins, on-chain data
- **Commodities:** Gold, silver, oil, soft commodities
- **Macro:** Fed policy, interest rates, inflation, DXY, liquidity cycles
- **Equities:** Stocks, indices, sector rotation
- **Forex:** Currency pairs, emerging markets
- **Geopolitics:** Events affecting market structure
- **Strategy:** Portfolio allocation, risk management, entry/exit frameworks

---

## What This Skill Does NOT Do

- Give single-point price predictions without scenarios
- Express certainty without evidence
- Omit the risk or invalidation condition
- Tell you what to do — it gives you a framework to decide

If output violates any of these → the system flags `⚠️ INSUFFICIENT EDGE` and re-evaluates before responding.

---

## Architecture

```
Input (market question)
│
├── Genesis Protocol
│   ├── First Principle Codex (root cause decomposition)
│   ├── System Thinking (micro → macro chain)
│   └── AI Fluency 4D (bias check + discernment)
│
├── SMC Layer Engine
│   ├── Market structure mapping
│   ├── Liquidity zone identification
│   └── Smart money vs. retail narrative separation
│
├── Scenario Engine
│   ├── Bull / Bear / Base case
│   ├── Entry-exit zones
│   └── Invalidation conditions
│
└── Output (LIGHT or FULL mode)
```

---

## File Structure

```
money-atlas-intelligence-os/
├── SKILL.md                    ← Claude skill definition (main entry point)
├── skill_config.json           ← Skill metadata and trigger config
├── architecture.md             ← System architecture overview
├── system_prompt.txt           ← Session boot prompt
├── full_mode.txt               ← Full mode output spec
├── light_mode.txt              ← Light mode output spec
│
├── core/                       ← Genesis Protocol engine
│   ├── genesis_core.py
│   ├── ai_fluency_4d.py
│   ├── discernment_engine.py
│   └── decision_engine.py
│
├── agents/                     ← Specialist agent layer
│   ├── orchestrator.py
│   ├── analyst_agent.py
│   ├── macro_agent.py
│   ├── smc_agent.py
│   ├── risk_agent.py
│   ├── sentiment_agent.py
│   ├── skeptic_agent.py
│   └── strategist_agent.py
│
├── smc/                        ← Smart Money Concept engine
├── intelligence/               ← Alpha, macro, geopolitics engines
├── strategy/                   ← Scenario + asymmetric opportunity engine
├── execution/                  ← Signal, risk, trade logging
├── orchestrator/               ← Multi-agent coordination
└── cli/                        ← Command-line runners
```

---

## How to Install (Claude Custom Skill)

1. Clone or download this repository
2. Place the `money-atlas-intelligence-os/` folder in your Claude skills directory
3. The skill activates automatically when Claude detects relevant financial market questions
4. Or call it explicitly by referencing the skill name in your system prompt

---

## Non-Negotiable Constraints

Every output must include:

- **Multiple scenarios** — no single prediction
- **Explicit uncertainty** — confidence level + key unknowns
- **Invalidation point** — what breaks the entire analysis
- **Human decision primacy** — the skill advises, the human decides

Violation of any constraint → output is invalid → re-evaluate.

---

## Part of the Skynet Skill Ecosystem

This skill operates within the broader **Skynet Elite Commander** meta-intelligence system:

| Skill | Domain |
|---|---|
| `skynet-elite-commander` | Meta-cognition OS — routes all domains |
| `money-atlas-intelligence-os` | Financial markets, macro, trading |
| `alternative-coffee-intelligence` | Coffee science and roastery operations |
| `genesis-mind-strategic-intelligence` | Strategic thinking, business, philosophy |
| `first-principle-codex-os` | Anti-hallucination cognitive base layer |

---

## ⚠️ Not financial advice

This system **analyses** markets. It does not advise. Its output is structured scenarios with
explicit uncertainty — an analytical instrument, not a recommendation, and it can be wrong.
You are solely responsible for your own decisions. Consult a licensed financial adviser before
acting on any output, and never deploy it against capital you cannot afford to lose.
See [NOTICE](NOTICE) and the warranty disclaimer in the [LICENSE](LICENSE).

---

## License

**[Apache License 2.0](LICENSE)** — OSI-approved, with an express patent grant. Free to use,
modify, and redistribute, including commercially at any revenue. Keep the licence and
[NOTICE](NOTICE), and state any changed files.

Attribution is requested (not required beyond NOTICE):
**Built on Money Atlas Intelligence OS by Bunyawat Dechanon (ElmatadorZ)**

Apache §6 grants no rights to the name: a derivative that removes the uncertainty disclosure,
the scenario structure, or the refusal to present analysis as advice must be renamed.

*(Earlier releases used the custom Open Cognitive License v1.0 with a 2% clause above $10M/year;
it was replaced to remove adoption friction. Prior text is in the git history.)*

---

## Author

**Bunyawat Dechanon**  
Independent Builder & Architect  
Brand: Alternative Slowbar / Money Atlas  
Location: Thailand

> *"The market is always telling a story. This skill helps you read who wrote it."*
