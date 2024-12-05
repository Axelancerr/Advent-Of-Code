import re

from common import input_line, print_results


def part_one():
    return sum(map(
        lambda equation: int.__mul__(*equation),
        map(
            lambda match: map(int, match),
            re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_line())
        )
    ))

def part_two():
    return [
        globals().__setitem__("enabled", True),
        sum(filter(
            lambda x: isinstance(x, int),
            map(
                lambda match:
                    globals().__setitem__(
                        "enabled",
                        False if match[0] == "don't()" else True if match[0] == "do()" else globals().get("enabled")
                    ) if match[0] != ""
                    else int(match[1]) * int(match[2]) if globals().get("enabled") is True
                    else None,
                re.findall(r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", input_line())
            )
        ))
    ][1]

print_results(part_one, part_two)
