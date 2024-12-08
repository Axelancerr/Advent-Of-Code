import itertools
import operator

from common import lines, print_results


def common(operators):
    equations = map(
        lambda x: [int(x[0]), [*map(int, x[1].strip().split(" "))]],
        map(
            lambda line: line.strip().split(":"),
            lines()
        )
    )
    total = 0
    for result, numbers in equations:
        for combo in itertools.product(operators, repeat=len(numbers) - 1):
            test_result = numbers[0]
            for index, op in enumerate(combo):
                test_result = op(test_result, numbers[index + 1])
            if test_result == int(result):
                total += int(result)
                break
    return total

def part_one():
    return common([operator.add, operator.mul])

def part_two():
    return common([operator.add, operator.mul, lambda x, y: int(str(x) + str(y))])

print_results(part_one, part_two)
