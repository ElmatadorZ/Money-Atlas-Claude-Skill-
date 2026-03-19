import json
from datetime import datetime

class TradeLogger:

    def log(self, signal, result):

        log_entry = {
            "time": datetime.utcnow().isoformat(),
            "symbol": signal.symbol,
            "direction": signal.direction,
            "entry": signal.entry,
            "sl": signal.stop_loss,
            "tp": signal.take_profit,
            "confidence": signal.confidence,
            "result": result
        }

        with open("trade_log.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
