import time


class RateLimiter:
    def __init__(self, limit, window_seconds, clock=time.monotonic):
        self.limit = limit
        self.window_seconds = window_seconds
        self.clock = clock
        self.windows = {}

    def allow(self, key):
        now = self.clock()
        start, count = self.windows.get(key, (now, 0))

        if now - start >= self.window_seconds:
            start, count = now, 0

        if count >= self.limit:
            return False

        self.windows[key] = (start, count + 1)
        return True
