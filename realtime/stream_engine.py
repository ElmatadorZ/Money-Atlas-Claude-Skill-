# realtime/stream_engine.py

import time

class StreamEngine:

    def run(self, callback, interval=10):

        while True:
            callback()
            time.sleep(interval)
