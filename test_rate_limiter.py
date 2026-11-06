from rate_limiter import RateLimiter


class FakeClock:
    def __init__(self):
        self.now = 0

    def __call__(self):
        return self.now


def make_limiter():
    clock = FakeClock()
    return RateLimiter(limit=3, window_seconds=10, clock=clock), clock


def test_allows_requests_up_to_limit():
    limiter, _ = make_limiter()
    assert [limiter.allow("user") for _ in range(3)] == [True, True, True]


def test_blocks_burst_over_limit():
    limiter, _ = make_limiter()
    results = [limiter.allow("user") for _ in range(4)]
    assert results == [True, True, True, False]


def test_resets_after_window():
    limiter, clock = make_limiter()
    for _ in range(3):
        limiter.allow("user")
    clock.now = 10
    assert limiter.allow("user") is True


def test_keys_are_independent():
    limiter, _ = make_limiter()
    for _ in range(3):
        limiter.allow("user-a")
    assert limiter.allow("user-b") is True
