import collections

from common import input_line, print_results


def part_1():
    rules_and_updates = input_line().split("\n\n")

    rules = collections.defaultdict(list)
    for rule in rules_and_updates[0].split("\n"):
        rule = rule.split("|")
        rules[rule[0]].append(rule[1])

    valid = []
    for update in rules_and_updates[1].split("\n"):
        update = update.split(",")
        y = []
        for index, page in enumerate(update):
            if [x for x in update[index + 1:] if x not in rules[page]]:
                break
            else:
                y.append(page)
                continue
        if y == update:
            valid.append(update)

    total = 0
    for update in valid:
        total += int(update[len(update) // 2])

    return total

def part_2():
    rules_and_updates = input_line().split("\n\n")

    rules = collections.defaultdict(set)
    for rule in rules_and_updates[0].split("\n"):
        rule = rule.split("|")
        rules[rule[0]].add(rule[1])

    invalids = []
    for update in rules_and_updates[1].split("\n"):
        update = update.split(",")
        for index, page in enumerate(update):
            if [x for x in update[index + 1:] if x not in rules[page]]:
                invalids.append(update)
                break

    sorteds = []
    for invalid in invalids:
        sort = [invalid[0]]
        for page in invalid[1:]:
            insert_at = 0
            for s in sort:
                if page in rules[s]:
                    insert_at += 1
            sort.insert(insert_at, page)
        sorteds.append(sort)

    valid = []
    for update in sorteds:
        y = []
        for index, page in enumerate(update):
            if [x for x in update[index + 1:] if x not in rules[page]]:
                break
            else:
                y.append(page)
                continue
        if y == update:
            valid.append(update)

    total = 0
    for update in valid:
        total += int(update[len(update) // 2])

    return total

print_results(part_1, part_2)
