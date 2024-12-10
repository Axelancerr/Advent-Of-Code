from copy import deepcopy

from common import line, print_results, time_results


def part_one():
    blocks = []
    for index, x in enumerate(line().strip()):
        if (index + 1) % 2 == 0:
            blocks.extend(["."] * int(x))
        else:
            blocks.extend([str(index // 2)] * int(x))

    sorted_blocks = []
    for i in range(len(blocks)):
        if i >= len(blocks):
            break

        if blocks[i] != ".":
            sorted_blocks.append(blocks[i])
            continue

        last = None
        j = 1
        while last is None:
            last = blocks[-j] if blocks[-j] != "." else None
            j += 1

        sorted_blocks.append(last)
        blocks = blocks[:-j + 1]

    checksum = 0
    for index, block in enumerate(sorted_blocks):
        checksum += index * int(block)
    return checksum

def part_two():
    blocks = []
    for index, x in enumerate(line().strip()):
        if (index + 1) % 2 == 0:
            blocks.append(["."] * int(x))
        else:
            blocks.append([str(index // 2)] * int(x))

    sorted_blocks = deepcopy(blocks)
    for end_block_index in [*range(len(blocks))][::-1]:
        end_block = sorted_blocks[end_block_index]
        if "." in end_block or len(end_block) == 0:
            continue
        for start_block_index in range(end_block_index):
            start_block = sorted_blocks[start_block_index]
            if "." not in start_block:
                continue
            if len(end_block) > len(start_block):
                continue
            if start_block.count(".") < len(end_block):
                continue
            sorted_blocks[start_block_index] = start_block[len(end_block):] + end_block
            sorted_blocks[end_block_index] = ["."] * len(end_block)
            break

    for index, sorted_block in enumerate(sorted_blocks):
        try:
            if sorted_block[0] == ".":
                sorted_blocks[index] = sorted_block[::-1]
        except IndexError:
            pass

    checksum = 0
    for index, block in enumerate([b for b in sorted_blocks for b in b]):
        if block.isnumeric():
            checksum += index * int(block)
    return checksum

print_results(part_one, part_two)