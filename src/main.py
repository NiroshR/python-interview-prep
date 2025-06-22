import argparse
from typing import Any
from business_logic import some_function


def parse_args(args: list[str] | None = None) -> dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument("--some-arg", "-s", type=int)
    return vars(parser.parse_args(args=args))


def run(some_arg: int):
    print("Hello, World!")
    print(f"{some_arg=}")
    some_function()


def main() -> None:
    args = parse_args()
    run(**args)


if __name__ == "__main__":
    main()
