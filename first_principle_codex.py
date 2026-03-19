# first_principle_codex.py
# ------------------------------------------------------------
# Genesis Protocol: First Principle Reasoning Kernel
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict, Any


# ============================================================
# 1) Atomic Truth Layer
# ============================================================

@dataclass
class AtomicTruth:
    statement: str
    certainty: float  # 0..1
    source: str       # data / logic / empirical


# ============================================================
# 2) Problem Decomposition
# ============================================================

def decompose_problem(problem: str) -> List[str]:
    """
    Break problem into irreducible components
    """
    # Simple version (can upgrade with LLM later)
    return [
        f"What are the fundamental parts of: {problem}?",
        f"What must be true for {problem} to exist?",
        f"What constraints define {problem}?"
    ]


# ============================================================
# 3) Extract Atomic Truths
# ============================================================

def extract_atomic_truths(context: Dict[str, Any]) -> List[AtomicTruth]:
    """
    Convert raw context into irreducible truths
    """
    truths = []

    for k, v in context.items():
        if isinstance(v, (int, float, str)):
            truths.append(AtomicTruth(
                statement=f"{k} = {v}",
                certainty=0.9,
                source="data"
            ))

    return truths


# ============================================================
# 4) Constraint Engine
# ============================================================

def derive_constraints(truths: List[AtomicTruth]) -> List[str]:
    constraints = []
    for t in truths:
        constraints.append(f"If {t.statement}, then system must respect it")
    return constraints


# ============================================================
# 5) Reconstruction Engine
# ============================================================

def reconstruct_solutions(truths: List[AtomicTruth]) -> List[str]:
    """
    Build solutions from ground up
    """
    solutions = []

    for t in truths:
        solutions.append(f"Exploit: {t.statement}")

    return solutions


# ============================================================
# 6) Contradiction Detector
# ============================================================

def detect_contradictions(truths: List[AtomicTruth]) -> List[str]:
    issues = []

    for i in range(len(truths)):
        for j in range(i + 1, len(truths)):
            if truths[i].statement == truths[j].statement:
                continue

            # naive contradiction check
            if ">" in truths[i].statement and "<" in truths[j].statement:
                issues.append(f"Conflict between {truths[i]} and {truths[j]}")

    return issues


# ============================================================
# 7) Codex Execution
# ============================================================

def run_first_principle_codex(problem: str, context: Dict[str, Any]) -> Dict[str, Any]:

    decomposition = decompose_problem(problem)
    truths = extract_atomic_truths(context)
    constraints = derive_constraints(truths)
    solutions = reconstruct_solutions(truths)
    contradictions = detect_contradictions(truths)

    return {
        "problem": problem,
        "decomposition": decomposition,
        "atomic_truths": [t.statement for t in truths],
        "constraints": constraints,
        "solutions": solutions,
        "contradictions": contradictions
    }
