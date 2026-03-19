# integration/macro_api.py

class MacroAPI:

    def get_macro_state(self):

        # mock → replace with FRED / TradingEconomics later
        return {
            "interest_rate": 5.25,
            "inflation": 3.2,
            "liquidity": "tightening"
        }
