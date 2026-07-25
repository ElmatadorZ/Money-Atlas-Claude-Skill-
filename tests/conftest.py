"""Shared test fixtures for Money Atlas Intelligence OS.

The repository root is importable so tests can exercise the reasoning modules
directly (first_principle_codex, analyzer, signals, core) without installing the
package.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@dataclass
class FakeLayer:
    """A minimal stand-in for an SMC layer.

    The analyzer/signal/insight engines duck-type on these attributes, so the
    tests can drive them without the async SMCLayerEngine or any market data.
    """
    layer: int = 1
    state: str = "accumulating"      # accumulating | distributing | ranging
    confidence: float = 0.8
    cost_basis: float = 100.0
    price_low: float = 95.0
    price_high: float = 105.0


@pytest.fixture
def accumulating_layer() -> FakeLayer:
    return FakeLayer(layer=1, state="accumulating", confidence=0.82, cost_basis=100.0)


@pytest.fixture
def distributing_layer() -> FakeLayer:
    return FakeLayer(layer=3, state="distributing", confidence=0.40, cost_basis=140.0)
