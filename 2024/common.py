import timeit
from collections.abc import Callable
from typing import Any


__all__ = [
    "print_results", "time_results",
    "lines", "line",
    "string_grid", "int_grid",
    "is_pos_in_grid"
]

def print_results(*parts: Callable[..., Any]) -> None:
    for i, part in enumerate(parts, 1):
        print(f"Part {i}: {part()}")

def time_results(*parts: Callable[..., Any], count: int = 5000) -> None:
    for i, part in enumerate(parts, 1):
        print(
            f"Part {i}: {part()} "
            f"({((timeit.timeit(part, number=count) / count) * 1000000):.2f}µs @ {count:,} runs)"
        )

lines: Callable[[], list[str]] = lambda: open("input.txt").readlines()
line: Callable[[], str] = lambda: open("input.txt").read()

string_grid: Callable[[], list[list[str]]] = lambda: [*map(
    lambda x: list(x),
    [*map(str.strip, lines())]
)]
int_grid: Callable[[], list[list[int]]] = lambda: [*map(
    lambda x: [*map(int, x)],
    [*map(str.split, lines())]
)]

def is_pos_in_grid(x: int, y: int, *, rows: int, cols: int) -> bool:
    return 0 <= x < rows and 0 <= y < cols