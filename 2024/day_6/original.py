from copy import deepcopy

from common import input_lines, time_results


dir_offsets = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}
dir_mapping = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

def common():
    grid = [[*line.strip()] for line in input_lines()]
    row_count, col_count = len(grid), len(grid[0])
    row_with_guard = [row for row in grid if "^" in row][0]
    guard_row, guard_col = grid.index(row_with_guard), row_with_guard.index("^")

    while True:
        guard_dir = grid[guard_row][guard_col]
        next_x = guard_row + dir_offsets[guard_dir][0]
        next_y = guard_col + dir_offsets[guard_dir][1]
        if (next_x < 0 or next_x >= row_count) or (next_y < 0 or next_y >= col_count):
            grid[guard_row][guard_col] = "X"
            break
        match (grid[next_x][next_y]):
            case "." | "X":
                grid[next_x][next_y] = guard_dir
                grid[guard_row][guard_col] = "X"
                guard_row, guard_col = next_x, next_y
            case "#":
                grid[guard_row][guard_col] = dir_mapping[guard_dir]
    return grid

def part_one():
    return sum(row.count("X") for row in common())

def part_two():
    _grid = [[*line.strip()] for line in input_lines()]
    row_count, col_count = len(_grid), len(_grid[0])

    def grids():
        for row in range(row_count):
            for col in range(col_count):
                if _grid[row][col] != ".":
                    continue
                copy = deepcopy(_grid)
                copy[row][col] = "#"
                yield copy

    count = 0
    for grid in grids():
        loops = 0

        row_with_guard = [row for row in grid if "^" in row][0]
        guard_row, guard_col = grid.index(row_with_guard), row_with_guard.index("^")

        while loops <= 6000:
            guard_dir = grid[guard_row][guard_col]
            next_x = guard_row + dir_offsets[guard_dir][0]
            next_y = guard_col + dir_offsets[guard_dir][1]
            if (next_x < 0 or next_x >= row_count) or (next_y < 0 or next_y >= col_count):
                grid[guard_row][guard_col] = "X"
                break
            match (grid[next_x][next_y]):
                case "." | "X":
                    grid[next_x][next_y] = guard_dir
                    grid[guard_row][guard_col] = "X"
                    guard_row, guard_col = next_x, next_y
                case "#":
                    grid[guard_row][guard_col] = dir_mapping[guard_dir]
            loops += 1
        else:
            if loops < 6000:
                continue
            count += 1

    return count

time_results(part_one, part_two, count=1)
