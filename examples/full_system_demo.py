# examples/full_system_demo.py

import asyncio
from agents.orchestrator import Orchestrator
from smc.smc_layer_masterpiece import load_ohlcv_csv

async def main():

    candles = load_ohlcv_csv("examples/sample_data.csv")

    context = {
        "symbol": "BTCUSDT",
        "timeframe": "4H",
        "candles": candles,
        "macro_data": {}
    }

    system = Orchestrator()

    result = await system.run(context)

    print("\n=== FINAL INTELLIGENCE ===")
    for k, v in result.items():
        print(k, ":", v)

asyncio.run(main())
