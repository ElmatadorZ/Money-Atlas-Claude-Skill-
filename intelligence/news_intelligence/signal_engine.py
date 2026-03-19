class SignalEngine:

    def generate(self, impact, smc_layers):

        signals = []

        for l in smc_layers:

            for i in impact:

                if l.state == "accumulating" and i["direction"] == "bullish":

                    signals.append({
                        "type": "HIGH_CONVICTION_SETUP",
                        "logic": "Narrative + Smart Money alignment",
                        "layer": l.layer
                    })

        return signals
