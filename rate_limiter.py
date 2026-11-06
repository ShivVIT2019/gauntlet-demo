from collections import defaultdict, deque
import time


class RateLimiter:
    def __init__(self, limit, window_seconds, clock=time.monotonic):
        self.limit = limit
        self.window_seconds = window_seconds
        self.clock = clock
        self.requests = defaultdict(deque)

    def allow(self, key):
        now = self.clock()
        timestamps = self.requests[key]

        # A request stops counting once it is a full window old.
        while timestamps and now - timestamps[0] >= self.window_seconds:
            timestamps.popleft()

        if len(timestamps) >= self.limit:
            return False

        timestamps.append(now)
        return True
