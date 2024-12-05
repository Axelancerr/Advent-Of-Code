import timeit
from collections.abc import Callable
from typing import Any


__all__ = [
    "input_lines", "input_line",
    "print_results", "time_results"
]

def input_lines() -> list[str]:
    return open("input.txt").readlines()

def input_line() -> str:
    return open("input.txt").read()

def print_results(*parts: Callable[[], Any]):
    for i, part in enumerate(parts, 1):
        print(f"Part {i}: {part()}")

def time_results(*parts: Callable[[], Any], count: int = 5000):
    for i, part in enumerate(parts, 1):
        print(
            f"Part {i}: {part()} "
            f"({((timeit.timeit(part, number=count) / count) * 1000000):.2f}µs @ {count:,} runs)"
        )
