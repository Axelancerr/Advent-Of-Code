(
    lambda windowed_depths:
        print(sum(1 if depth > windowed_depths[index - 1] else 0 for index, depth in enumerate(windowed_depths)))
)(
    (
        lambda depths:
            [sum(depths[i: i + 3]) for i in range(len(depths) - 2)]
    )(
        list(map(int, open("input.txt").readlines()))
    )
)
