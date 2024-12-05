from common import print_results


def part_one():
    a = [*map(str.split, open("input.txt").readlines())]
    b = zip(sorted([int(x[0]) for x in a]), sorted([int(x[1]) for x in a]))
    c = [abs(x[0] - x[1]) for x in b]
    return sum(c)

def part_two():
    a = [*map(str.split, open("input.txt").readlines())]
    b = [x[0] for x in a], [x[1] for x in a]
    c = [int(x) * b[1].count(x) for x in b[0]]
    return sum(map(int, c))

print_results(part_one, part_two)
