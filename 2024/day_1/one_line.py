import collections

from common import input_lines, print_results


locations = [*map(str.split, input_lines())]
lefts = [*map(lambda x: int(x[0]), locations)]
rights = [*map(lambda x: int(x[1]), locations)]

def part_one():
    return sum(map(
        lambda location: abs(location[0] - location[1]),
        zip(sorted(lefts), sorted(rights))
    ))

def part_two():
    return [
        count := collections.Counter(rights),
        sum([left * count[left] for left in lefts])
    ][1]

print_results(part_one, part_two)
