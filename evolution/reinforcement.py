# evolution/reinforcement.py

class ReinforcementEngine:

    def update(self, decisions, performance):
        for d in decisions:
            d["weight"] = d.get("weight", 1.0)

            if performance > 0.7:
                d["weight"] *= 1.1
            elif performance < 0.5:
                d["weight"] *= 0.9

        return decisions
