import time


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
    time.sleep(1)
    print("here")


def multiply_by_two(x: int) -> int:
    return x * 2
