import itertools

from common import int_grid, print_results


check = lambda report: (
    any([
        sorted(report) == report,
        sorted(report) == report[::-1]
    ])
    and
    all(map(
        lambda i: (1 <= abs(report[i] - report[i + 1]) <= 3),
        range(len(report) - 1)
    ))
)

def part_one():
    return len([*filter(check, int_grid())])

def part_two():
    return len([*filter(
        lambda report: [*filter(
            check,
            map(list, itertools.combinations(report, len(report) - 1))
        )],
        int_grid()
    )])

print_results(part_one, part_two)
