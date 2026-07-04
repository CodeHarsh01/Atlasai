import time
from typing import Callable


def retry(
    func: Callable,
    *args,
    retries: int = 3,
    delay: int = 2,
    **kwargs
):

    last_error: Exception | None = None

    for attempt in range(retries):

        try:

            return func(*args, **kwargs)

        except Exception as error:

            last_error = error

            if attempt < retries - 1:

                time.sleep(delay)

    if last_error:

        raise last_error

    raise RuntimeError("Unknown retry failure.")