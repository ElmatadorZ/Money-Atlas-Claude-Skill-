# smc/smc_wrapper.py

from typing import Dict, Any
from .smc_layer_masterpiece import SMCLayerEngine


class SMCWrapper:

    def __init__(self):
        self.engine = SMCLayerEngine()

    async def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:

        result = await self.engine.analyze(
            symbol=context["symbol"],
            timeframe=context["timeframe"],
            candles=context["candles"]
        )

        layers = []

        for layer in result.layers:
            layers.append({
                "layer": layer.layer,
                "range": (layer.price_low, layer.price_high),
                "state": layer.state,
                "confidence": layer.confidence
            })

        return {
            "layers": layers,
            "summary": self._interpret_layers(layers)
        }

    def _interpret_layers(self, layers):

        if not layers:
            return "No structure detected"

        l1 = layers[0]
        l5 = layers[-1]

        return f"Market spans from accumulation ({l1['range']}) to distribution ({l5['range']})"
