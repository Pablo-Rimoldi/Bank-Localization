from typing import TypeVar, Callable

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


F = TypeVar("F", bound=Callable[..., object])


def with_retries(max_attempts: int = 3) -> Callable[[F], F]:
    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((TimeoutError, ConnectionError)),
        reraise=True,
    )


