"""First Principle Codex — the reasoning kernel that separates observed truth
from inference. These tests lock its contract: what it extracts, what it treats
as certain, and that the full pipeline stays internally consistent.
"""
from __future__ import annotations

import first_principle_codex as fpc


def test_decompose_returns_irreducible_questions():
    parts = fpc.decompose_problem("BTC direction")
    assert isinstance(parts, list) and len(parts) >= 3
    # Every component is a question about the problem, not a restatement of it.
    assert all("BTC direction" in p and p.endswith("?") for p in parts)


def test_atomic_truths_only_from_scalar_context():
    truths = fpc.extract_atomic_truths(
        {"price": 100, "trend": "up", "note": ["a", "list"], "meta": {"k": "v"}}
    )
    statements = [t.statement for t in truths]
    # Scalars become truths; containers are not invented into facts.
    assert "price = 100" in statements
    assert "trend = up" in statements
    assert not any("list" in s or "meta" in s for s in statements)


def test_data_sourced_truths_are_not_certain():
    # A value read from context is high- but not full-certainty, and is labelled
    # as data — the K/I/U discipline the whole ecosystem rests on.
    truths = fpc.extract_atomic_truths({"cpi": 3.1})
    assert len(truths) == 1
    assert truths[0].source == "data"
    assert 0.0 < truths[0].certainty < 1.0


def test_constraints_track_every_truth():
    truths = fpc.extract_atomic_truths({"a": 1, "b": 2})
    constraints = fpc.derive_constraints(truths)
    assert len(constraints) == len(truths)


def test_contradiction_detector_flags_gt_vs_lt():
    truths = [
        fpc.AtomicTruth("price > 100", 0.9, "data"),
        fpc.AtomicTruth("price < 90", 0.9, "data"),
    ]
    assert fpc.detect_contradictions(truths)


def test_no_false_contradiction_on_aligned_truths():
    truths = [
        fpc.AtomicTruth("price > 100", 0.9, "data"),
        fpc.AtomicTruth("volume > 1000", 0.9, "data"),
    ]
    assert fpc.detect_contradictions(truths) == []


def test_full_pipeline_shape():
    out = fpc.run_first_principle_codex("gold outlook", {"spot": 2400, "real_yield": -0.5})
    for key in ("problem", "decomposition", "atomic_truths",
                "constraints", "solutions", "contradictions"):
        assert key in out
    assert out["problem"] == "gold outlook"
    assert "spot = 2400" in out["atomic_truths"]
    # constraints and solutions are derived one-per-truth, so they stay in step.
    assert len(out["constraints"]) == len(out["atomic_truths"])
    assert len(out["solutions"]) == len(out["atomic_truths"])
