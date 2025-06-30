import json
import time
from urllib3.util.retry import Retry
from urllib3 import PoolManager

def some_decorator(_: None = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)

            end = time.time()
            print(f"{func.__name__} returned {result}, took {end - start} second(s)")
            return result

        return wrapper

    return decorator


@some_decorator()
def some_function():
    print("here")

    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503])
    # Connection is reused → faster + scalable
    http = PoolManager(retries=retries)
    # _ = http.request("GET", "https://httpbin.org/status/500")

    resp = http.request(
        "POST",
        "https://httpbin.org/post",
        fields={"hello": "world"} #  Add custom form fields
    )

    data = json.loads(resp.data)
    print(data)


def multiply_by_two(x: int) -> int:
    return x * 2
