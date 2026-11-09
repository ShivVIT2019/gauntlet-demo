import time
from collections import deque


class RateLimiter:
    def __init__(self, limit, window_seconds, clock=time.monotonic):
        self.limit = limit
        self.window_seconds = window_seconds
        self.clock = clock
        self.windows = {}

    def allow(self, key):
        now = self.clock()
        requests = self.windows.setdefault(key, deque())

        # Keep accepted requests within the rolling window.
        while requests and now - requests[0] >= self.window_seconds:
            requests.popleft()

        if len(requests) >= self.limit:
            return False

        requests.append(now)
        return True
