
def part_one() -> None:
    a = [*map(str.split, open("input.txt").readlines())]
    b = zip(sorted([int(x[0]) for x in a]), sorted([int(x[1]) for x in a]))
    c = [abs(x[0] - x[1]) for x in b]
    print(sum(c))

def part_two() -> None:
    a = [*map(str.split, open("input.txt").readlines())]
    b = [x[0] for x in a], [x[1] for x in a]
    c = [int(x) * b[1].count(x) for x in b[0]]
    print(sum(map(int, c)))



part_one()
part_two()