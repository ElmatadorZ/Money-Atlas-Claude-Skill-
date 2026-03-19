class ScenarioEngine:

    def simulate(self, smc_layers):

        scenarios = []

        for layer in smc_layers:

            if layer.state == "accumulating":
                scenarios.append({
                    "scenario": "Bullish Continuation",
                    "description": "ราคามีโอกาสปรับตัวขึ้นต่อ",
                    "confidence": layer.confidence
                })

            elif layer.state == "distributing":
                scenarios.append({
                    "scenario": "Bearish Reversal",
                    "description": "ราคามีโอกาสกลับตัวลง",
                    "confidence": layer.confidence
                })

        return scenarios
