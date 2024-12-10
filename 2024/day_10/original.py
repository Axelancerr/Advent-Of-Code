from common import print_results, string_grid


def part_one():
    grid = string_grid()

    def check_neighbors(_row, _col, _expected=1, _visited=None):
        if _visited is None:
            _visited = set()
        for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            r, c = _row + offset[0], _col + offset[1]
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue
            if grid[r][c] == str(_expected):
                _visited.add((grid[r][c], r, c))
                if _expected == 10:
                    break
                check_neighbors(r, c, _expected + 1, _visited=_visited)
        return _visited

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            trailhead = grid[row][col]
            if trailhead != "0":
                continue
            total += len([x for x in check_neighbors(row, col) if x[0] == "9"])
    return total

def part_two():
    grid = string_grid()
    paths = {}

    def check_neighbors(_row, _col, _expected=1, _visited=None):
        if _visited is None:
            _visited = []
        for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            r, c = _row + offset[0], _col + offset[1]
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue
            if grid[r][c] == str(_expected):
                _visited.append((grid[r][c], r, c))
                check_neighbors(r, c, _expected + 1, _visited=_visited)
                if grid[r][c] == "9":
                    path = (grid[row][col], row, col), (grid[r][c], r, c)
                    if path in paths:
                        paths[path] += 1
                    else:
                        paths[path] = 1
        return _visited

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            trailhead = grid[row][col]
            if trailhead != "0":
                continue
            check_neighbors(row, col)
    total += sum(paths.values())
    return total

print_results(part_one, part_two)
