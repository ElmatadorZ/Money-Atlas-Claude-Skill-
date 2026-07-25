"""The SMC-layer engines: signal, risk, insight, decision.

These are the pieces that turn market structure into a recommendation, so their
gates are exactly where a mistake would cost money. The tests pin the gates:
a BUY only on high-confidence accumulation, risk raised on low confidence or
distribution, and a decision that maximises reward minus risk.
"""
from __future__ import annotations

from analyzer.insight_engine import InsightEngine
from analyzer.risk_engine import RiskEngine
from core.decision_engine import DecisionEngine
from signals.signal_engine import SignalEngine


def test_signal_fires_buy_only_on_confident_accumulation(accumulating_layer):
    sigs = SignalEngine().generate([accumulating_layer])
    assert len(sigs) == 1
    assert sigs[0]["type"] == "BUY"
    assert sigs[0]["price"] == accumulating_layer.cost_basis
    assert sigs[0]["confidence"] == accumulating_layer.confidence


def test_signal_withholds_on_low_confidence(accumulating_layer):
    accumulating_layer.confidence = 0.55   # below the 0.7 gate
    assert SignalEngine().generate([accumulating_layer]) == []


def test_signal_withholds_when_distributing(distributing_layer):
    distributing_layer.confidence = 0.9    # high confidence, wrong phase
    assert SignalEngine().generate([distributing_layer]) == []


def test_risk_flags_low_confidence(distributing_layer):
    risks = RiskEngine().evaluate([distributing_layer])
    # confidence 0.40 (< 0.5) AND distributing → two distinct risk notes.
    assert len(risks) == 2


def test_risk_silent_on_healthy_layer(accumulating_layer):
    assert RiskEngine().evaluate([accumulating_layer]) == []


def test_insight_distinguishes_accumulation_from_distribution(
    accumulating_layer, distributing_layer
):
    out = InsightEngine().generate([accumulating_layer, distributing_layer])
    assert len(out) == 2
    joined = " ".join(out)
    assert "สะสม" in joined       # accumulation note (Thai source strings)
    assert "แรงขาย" in joined     # distribution note


def test_decision_picks_best_reward_minus_risk():
    options = [
        {"name": "hold", "reward": 2, "risk": 1},
        {"name": "long", "reward": 9, "risk": 3},   # best net = 6
        {"name": "short", "reward": 4, "risk": 4},
    ]
    out = DecisionEngine().decide(options)
    assert out["decision"]["name"] == "long"
    assert "confidence" in out and "reason" in out
