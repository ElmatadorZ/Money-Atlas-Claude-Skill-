# data_pipeline/ingestion_engine.py

from integration.market_api import MarketAPI
from integration.macro_api import MacroAPI
from integration.news_api import NewsAPI

class IngestionEngine:

    def __init__(self):
        self.market = MarketAPI()
        self.macro = MacroAPI()
        self.news = NewsAPI()

    def fetch_all(self):

        return {
            "price": self.market.get_price(),
            "macro": self.macro.get_macro_state(),
            "news": self.news.get_headlines()
        }
