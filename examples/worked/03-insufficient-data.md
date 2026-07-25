# Worked example — honest degradation

**User:** Where's BTC headed? *(no chart, no price, no data attached)*

This is the case most skills fail: asked to predict with nothing to reason from,
they invent a price and a target. This one does not. It has no live feed by
design (`requires_tools: false`, `not_for` names real-time price), so it states
the framework and names the missing inputs.

---

**Output (shape):**

> **BTC — I can't give a directional read without inputs, but here is the frame.**
>
> A directional call needs at least: current price relative to the last
> accumulation range, the higher-timeframe trend structure, and whether the SMC
> layer shows accumulation or distribution. I don't have those.
>
> **What I can do right now:**
> - Lay out the two structural paths (continuation vs. range-break) and the
>   condition that decides between them.
> - Tell you exactly which three inputs would let me commit to one.
>
> **What I will not do:** quote a current price or a target I cannot source. An
> invented number is worse than an admitted gap.
>
> Give me the current price and the higher-timeframe structure and I'll return a
> LIGHT read with a confidence and an invalidation.

---

**Why it is shaped this way**

This is the behaviour the skill's *When information is insufficient* rule
requires, and the reason `metadata.not_for` names real-time price feeds: the skill
is a reasoning framework, not a data source. Abstaining is a valid output;
fabricating a level is a failure.
