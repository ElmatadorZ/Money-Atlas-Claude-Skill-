# agents/smc_agent.py

from .base_agent import BaseAgent, AgentOutput
from smc.smc_layer_masterpiece import SMCLayerEngine

class SMCAgent(BaseAgent):
    name = "smc"

    def __init__(self):
        self.engine = SMCLayerEngine()

    async def run(self, context):
        candles = context["candles"]

        result = await self.engine.analyze(
            symbol=context["symbol"],
            timeframe=context["timeframe"],
            candles=candles
        )

        return AgentOutput(
            name=self.name,
            data={"layers": result.layers},
            confidence=0.85,
            reasoning="SMC Layer structure detected"
        )
