from smc.smc_layer_masterpiece import SMCLayerEngine

class SMCAdapter:

    def __init__(self):
        self.engine = SMCLayerEngine()

    async def analyze(self, symbol, timeframe, candles):
        result = await self.engine.analyze(
            symbol=symbol,
            timeframe=timeframe,
            candles=candles
        )
        return result
