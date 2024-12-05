import itertools

from common import print_results


def part_one():
    return len([
        x for x in [[*map(int, line)] for line in map(str.split, open("input.txt").readlines())]
        if ((sorted(x) == x) or (sorted(x, reverse=True) == x))
        and all([(1 <= abs(x[i] - x[i + 1]) <= 3) for i in range(len(x) - 1)])
    ])

def part_two():
    lines = [[*map(int, line)] for line in map(str.split, open("input.txt").readlines())]
    correct = 0
    for line in lines:
        combos = map(list, itertools.combinations(line, len(line) - 1))
        if any([
            x for x in map(list, [*combos])
            if ((sorted(x) == x) or (sorted(x, reverse=True) == x))
            and all([(1 <= abs(x[i] - x[i + 1]) <= 3) for i in range(len(x) - 1)])
        ]):
            correct += 1
            continue
    return correct

print_results(part_one, part_two)
