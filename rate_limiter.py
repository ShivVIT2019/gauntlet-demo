import time


class RateLimiter:
    def __init__(self, limit, window_seconds, clock=time.monotonic):
        self.limit = limit
        self.window_seconds = window_seconds
        self.clock = clock
        self.windows = {}

    def allow(self, key):
        now = self.clock()
        recent = [t for t in self.windows.get(key, []) if now - t < self.window_seconds]

        if len(recent) >= self.limit:
            return False

        self.windows[key] = recent + [now]
        return True
