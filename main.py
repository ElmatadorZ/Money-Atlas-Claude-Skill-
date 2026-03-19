import asyncio

from smc.smc_layer_masterpiece import SMCLayerEngine
from execution.signal_engine import SignalEngine
from execution.risk_engine import RiskEngine
from execution.execution_engine import ExecutionEngine
from execution.broker_adapter import MockBroker
from execution.trade_logger import TradeLogger

async def run():

    # 1. Load Data
    candles = []  # ใส่ OHLCV จริง

    # 2. Analyze Market
    smc_engine = SMCLayerEngine()
    layer_map = await smc_engine.analyze(
        symbol="BTCUSDT",
        timeframe="4H",
        candles=candles
    )

    # 3. Generate Signal
    signal_engine = SignalEngine()
    signal = signal_engine.generate_signal(layer_map)

    if not signal:
        print("No Trade Signal")
        return

    # 4. Risk Management
    risk_engine = RiskEngine(capital=10000)

    # 5. Execute Trade
    broker = MockBroker()
    execution_engine = ExecutionEngine(broker, risk_engine)

    result = execution_engine.execute(signal)

    # 6. Log
    logger = TradeLogger()
    logger.log(signal, result)

asyncio.run(run())
