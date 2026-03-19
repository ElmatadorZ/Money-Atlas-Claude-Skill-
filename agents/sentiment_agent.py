# agents/sentiment_agent.py

from .base_agent import BaseAgent, AgentOutput

class SentimentAgent(BaseAgent):
    name = "sentiment"

    async def run(self, context):
        return AgentOutput(
            name=self.name,
            data={"sentiment": "greed"},
            confidence=0.6,
            reasoning="Market shows late-stage optimism"
        )
