from common import input_lines


locations = [*map(str.split, input_lines())]
lefts = [*map(lambda x: int(x[0]), locations)]
rights = [*map(lambda x: int(x[1]), locations)]

def part_one():
    print(sum(map(
        lambda location: abs(location[0] - location[1]),
        zip(sorted(lefts), sorted(rights))
    )))

def part_two():
    print(sum(map(
        lambda left: left * rights.count(left),
        lefts
    )))

part_one()
part_two()
