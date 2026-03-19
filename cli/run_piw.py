# cli/run_piw.py

from orchestrator.war_brain import WarBrain

def main():

    smc_layers = [
        type("Layer", (), {
            "state": "accumulating",
            "confidence": 0.8,
            "cost_basis": 1900,
            "layer": 1
        })()
    ]

    brain = WarBrain()
    result = brain.run(smc_layers)

    print(result)

if __name__ == "__main__":
    main()
