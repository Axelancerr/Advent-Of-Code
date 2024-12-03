(
    lambda _, _numbers, _boards, _1:
        print(_numbers)
)(
    inputs := list(map(str.strip, open("input.txt").readlines())),
    numbers := list(map(int, inputs.pop(0).split(","))),
    boards := [[list(map(int, x)) for x in map(str.split, group)] for matches, group in __import__("itertools").groupby(inputs, bool) if matches],
    find := (
        lambda myself:
            lambda index, inputs, what:
                myself(myself, index, inputs, what)
    )(
        lambda myself, index, inputs, what:
        (
            most_common := (i := __import__("collections").Counter([binary[index] for binary in inputs]).most_common())[
                (
                    0 if i[0][1] > i[1][1] else (0 if i[0][0] == "1" else 1)
                ) if what == "most" else (
                    1 if i[0][1] > i[1][1] else 0 if i[0][0] == "0" else 1
                )
            ][0],
            [inputs.remove(x) for x in [binary for binary in inputs if binary[index] != most_common]],
            None if len(inputs) == 1 else myself(myself, index + 1, inputs, what)
        )
    ),
)
