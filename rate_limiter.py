import time


class RateLimiter:
    def __init__(self, limit, window_seconds, clock=time.monotonic):
        self.limit = limit
        self.window_seconds = window_seconds
        self.clock = clock
        self.windows = {}

    def allow(self, key):
        now = self.clock()
        cutoff = now - self.window_seconds
        timestamps = [t for t in self.windows.get(key, []) if t > cutoff]

        if len(timestamps) >= self.limit:
            self.windows[key] = timestamps
            return False

        timestamps.append(now)
        self.windows[key] = timestamps
        return True
