import re

from common import input_line


def part_one():
    print(sum(map(
        lambda equation: int.__mul__(*equation),
        map(
            lambda match: map(int, match),
            re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_line())
        )
    )))

def part_two():
    print([
        globals().__setitem__("enabled", True),
        sum([
            x for x in [
                [
                    int(match[1]) * int(match[2]) if globals().get("enabled") and match[0] == "" else None,
                    globals().__setitem__(
                        "enabled",
                        False if match[0] == "don't()" else True if match[0] == "do()" else globals().get("enabled")
                    )
                ][0]
                for match in re.findall(r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", input_line())
            ] if isinstance(x, int)
        ])
    ][1])

part_one()
part_two()

def part_one():
    regex = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
    matches = regex.findall("".join(tests()))
    nums = [[int(x) for x in y.split(",")] for y in matches]
    print(sum([int.__mul__(*x) for x in nums]))