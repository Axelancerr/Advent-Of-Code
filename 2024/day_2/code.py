import itertools

from common import input_lines


reports = [[int(level) for level in report] for report in [line.split() for line in input_lines()]]
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
    print(len([*filter(check, reports)]))

def part_two():
    print(len(
        [*filter(
            lambda report: [*filter(
                check,
                map(list, itertools.combinations(report, len(report) - 1))
            )],
            reports
        )]
    ))

part_one()
part_two()
