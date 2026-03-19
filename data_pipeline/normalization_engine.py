# data_pipeline/normalization_engine.py

class NormalizationEngine:

    def process(self, raw):

        return {
            "price": raw["price"],
            "macro_bias": "bearish" if raw["macro"]["liquidity"] == "tightening" else "bullish",
            "geo_risk": any("risk" in n.lower() for n in raw["news"])
        }
