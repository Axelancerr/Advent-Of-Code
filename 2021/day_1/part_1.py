(
    lambda depths:
        print(sum(1 if depth > depths[index - 1] else 0 for index, depth in enumerate(depths)))
)(
    list(map(int, open("input.txt").readlines()))
)
