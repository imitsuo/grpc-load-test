"""utils.cache namespace."""

import time
from functools import lru_cache


@lru_cache(typed=True)
def _executor(ttl: int, func: callable, *args, **kwargs):
    del ttl
    return func(*args, **kwargs)


def cache_with_ttl(seconds: int = 60):
    """cache."""

    def wrap(func):
        def inner_function(*args, **kwargs):
            ttl = int(time.time() / seconds)
            return _executor(ttl, func, *args, **kwargs)

        return inner_function

    return wrap
