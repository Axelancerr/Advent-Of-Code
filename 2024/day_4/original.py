from numpy.lib._stride_tricks_impl import sliding_window_view

from common import is_pos_in_grid, print_results, string_grid


def part_1():
    word = "XMAS"
    grid = string_grid()
    rows = len(grid)
    columns = len(grid[0])
    offsets = [
        [0, 1], [0, -1],
        [1, 0], [-1, 0],
        [1, 1], [1, -1],
        [-1, 1], [-1, -1]
    ]
    count = 0
    for row in range(rows):
        for column in range(columns):
            for row_offset, column_offset in offsets:
                if all([
                    is_pos_in_grid(row + i * row_offset, column + i * column_offset, rows=rows, cols=columns)
                    and grid[row + i * row_offset][column + i * column_offset] == word[i]
                    for i in range(len(word))
                ]):
                    count += 1
    return count

def part_2():
    grid = string_grid()
    sub_grids = sliding_window_view(grid, (3, 3)).reshape(-1, 3, 3)
    valid_grids = [
        [["M", "", "M"],
         ["", "A", ""],
         ["S", "", "S"]],
        [["S", "", "S"],
         ["", "A", ""],
         ["M", "", "M"]],
        [["M", "", "S"],
         ["", "A", ""],
         ["M", "", "S"]],
        [["S", "", "M"],
         ["", "A", ""],
         ["S", "", "M"]]
    ]
    count = 0
    for sub_grid in sub_grids:
        for valid_grid in valid_grids:
            if all([
                valid_grid[row][column] == sub_grid[row][column]
                for row in range(3) for column in range(3) if valid_grid[row][column] != ""
            ]):
                count += 1
                break
    return count

print_results(part_1, part_2)
