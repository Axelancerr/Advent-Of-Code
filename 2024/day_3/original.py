import re

from common import input_lines, print_results


def part_one():
    regex = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
    matches = regex.findall("".join(input_lines()))
    nums = [[int(x) for x in y.split(",")] for y in matches]
    return sum([int.__mul__(*x) for x in nums])

def part_two():
    regex = re.compile(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")
    matches = regex.findall("".join(input_lines()))
    total = 0
    enabled = True
    for match in matches:
        if "do()" in match:
            enabled = True
        elif "don't()" in match:
            enabled = False
        if enabled and match[2] != "":
            total += (int(match[2]) * int(match[3]))
    return total

print_results(part_one, part_two)
