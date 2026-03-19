# signals/signal_engine.py

class SignalEngine:

    def generate(self, smc_layers):
        signals = []

        for layer in smc_layers:
            if layer.confidence > 0.7 and layer.state == "accumulating":
                signals.append({
                    "type": "BUY",
                    "price": layer.cost_basis,
                    "confidence": layer.confidence
                })

        return signals
