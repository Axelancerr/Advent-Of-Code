from collections import Counter

from common import line, print_results


def blink(stones):
    new = Counter()
    for stone, count in stones.items():
        if stone == 0:
            new[1] += count
        elif len(string := str(stone)) % 2 == 0:
            length = len(string)
            new[int(string[length // 2:])] += count
            new[int(string[:length // 2])] += count
        else:
            new[stone * 2024] += count
    return new

def part_one():
    stones = Counter(int(stone) for stone in line().split())
    for i in range(25):
        stones = blink(stones)
    return sum(stones.values())

def part_two():
    stones = Counter(int(stone) for stone in line().split())
    for i in range(75):
        stones = blink(stones)
    return sum(stones.values())

print_results(part_one, part_two)
