# Security Policy

## Reporting

Report privately via
[GitHub Security Advisories](https://github.com/ElmatadorZ/MoneyAtlas-ClaudeSkill-Agent/security/advisories/new).
**Acknowledgement within 7 days · initial assessment within 30 days.**

## In scope

### 1. Analytical integrity (most serious)
Because this system reasons about money, the highest-severity issues are those that cause it to
present unfounded output as sound:

- an input that makes the skill emit a recommendation **without** its required uncertainty
  disclosure or scenario structure
- a prompt that causes it to present analysis as **advice**, contrary to its stated contract
- prompt injection through untrusted market content (a pasted article, a news feed, a tool result)
  that redirects the analysis
- a path that bypasses the inherited FPCOS Shadow Gate (self-critique) before output

### 2. Execution safety
Defects in `execution/` — signal, risk, or broker-adapter logic — that could place, size, or route
an order incorrectly. Treat anything touching order flow as high severity by default.

### 3. Credential handling
Any path that logs, echoes, or persists an API key, broker credential, or account identifier.
Report privately and do **not** include the credential itself.

### 4. Tooling
Defects in `tools/validate_skill.py` or CI — for example, a validator reporting PASS on a skill.md
whose uncertainty requirements have been removed.

## Out of scope

- **Losing money on a trade.** Market outcomes are not vulnerabilities. This system is analysis,
  not advice, and can be wrong — see [NOTICE](NOTICE).
- Weaknesses of the underlying model (report to the model vendor).
- Third-party market-data or broker APIs (report to that provider).

## Supported versions

| Version | Supported |
|---|---|
| 2.x | ✅ |
