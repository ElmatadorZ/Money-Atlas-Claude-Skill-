# agents/orchestrator.py

import asyncio

from .macro_agent import MacroAgent
from .smc_agent import SMCAgent
from .sentiment_agent import SentimentAgent
from .risk_agent import RiskAgent
from .portfolio_agent import PortfolioAgent


class Orchestrator:

    def __init__(self):
        self.agents = [
            MacroAgent(),
            SMCAgent(),
            SentimentAgent(),
            RiskAgent(),
            GenesisAgent(),
            PortfolioAgent()
        ]

    async def run(self, context):

        results = {}

        for agent in self.agents:
            output = await agent.run(context)
            results[agent.name] = output.data
            context[agent.name] = output.data

        return results
