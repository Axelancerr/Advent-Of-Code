import itertools

from common import int_grid, print_results


def part_one():
    return len([
        x for x in int_grid()
        if ((sorted(x) == x) or (sorted(x, reverse=True) == x))
        and all([(1 <= abs(x[i] - x[i + 1]) <= 3) for i in range(len(x) - 1)])
    ])

def part_two():
    lines = int_grid()
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
