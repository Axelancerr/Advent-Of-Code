from common import is_pos_in_grid, print_results, string_grid


grid = string_grid()

def part_one():
    antennas = (
        ((x1, y1), (x2, y2))
        for x1 in range(len(grid)) for y1 in range(len(grid[x1]))
        if grid[x1][y1] != '.'
        for x2 in range(len(grid)) for y2 in range(len(grid[x2]))
        if (x1 != x2 or y1 != y2) and grid[x1][y1] == grid[x2][y2]
    )
    antinodes = set()
    for pair in antennas:
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        antinode1 = ((2 * x1) - x2), ((2 * y1) - y2)
        antinode2 = ((2 * x2) - x1), ((2 * y2) - y1)
        if is_pos_in_grid(*antinode1, rows=len(grid), cols=len(grid[0])):
            antinodes.add(antinode1)
        if is_pos_in_grid(*antinode2, rows=len(grid), cols=len(grid[0])):
            antinodes.add(antinode2)
    return len(antinodes)

def part_two():
    antenna_pairs = (
        ((x1, y1), (x2, y2))
        for x1 in range(len(grid)) for y1 in range(len(grid[x1]))
        if grid[x1][y1] != '.'
        for x2 in range(len(grid)) for y2 in range(len(grid[x2]))
        if (x1 != x2 or y1 != y2) and grid[x1][y1] == grid[x2][y2]
    )
    antinodes = set()
    for pair in antenna_pairs:
        antinodes.add(pair[0])
        antinodes.add(pair[1])
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        for i in range(2, 50):
            antinode1 = ((i * x1) - ((i - 1) * x2)), ((i * y1) - ((i - 1) * y2))
            antinode2 = ((i * x2) - ((i - 1) * x1)), ((i * y2) - ((i - 1) * y1))
            if is_pos_in_grid(*antinode1, rows=len(grid), cols=len(grid[0])):
                antinodes.add(antinode1)
            if is_pos_in_grid(*antinode2, rows=len(grid), cols=len(grid[0])):
                antinodes.add(antinode2)
    return len(antinodes)

print_results(part_one, part_two)
