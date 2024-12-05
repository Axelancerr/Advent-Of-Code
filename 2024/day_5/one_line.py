import collections
from typing import Iterator

from common import input_line, time_results


rules = collections.defaultdict(set)
updates = []

for line in input_line().split():
    if "|" in line:
        before, after = line.split("|")
        rules[before].add(after)
    elif "," in line:
        updates.append(line.split(","))

def find_valid_updates(_updates: list[list[str]]) -> Iterator[list[list[str]]]:
    return filter(
        lambda update: all(map(
            lambda page: all(map(
                lambda other_page: other_page in rules[page],
                update[update.index(page) + 1:]
            )),
            update
        )),
        _updates
    )

def part_1():
    return sum(map(
        lambda update: int(update[len(update) // 2]),
        find_valid_updates(updates)
    ))

def part_2():
    return sum(map(
        lambda _update: int(_update[len(_update) // 2]),
        find_valid_updates([
            invalid_updates := [*filter(
                lambda update: any(map(
                    lambda page: any(map(
                        lambda other_page: other_page not in rules[page],
                        update[update.index(page) + 1:]
                    )),
                    update
                )),
                updates
            )],
            sorted_updates := [*map(lambda x: [x[0]], invalid_updates)],
            [*map(
                lambda invalid_update: [
                    index := invalid_update[0],
                    invalid_update := invalid_update[1],
                    [*map(
                        lambda page: sorted_updates[index].insert(
                            sum(map(
                                lambda s: page in rules[s],
                                sorted_updates[index]
                            )),
                            page
                        ),
                        invalid_update
                    )]
                ][-1],
                enumerate([*map(lambda x: x[1:], invalid_updates)])
            )]
        ][1])
    ))

time_results(part_1, part_2)
