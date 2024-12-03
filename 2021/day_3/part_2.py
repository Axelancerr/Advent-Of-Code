(
    lambda oxygen_generator_rating, co2_scrubber_rating, _1, _2, _3:
        print(int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2))
)(
    input_1 := list(map(str.strip, open("input.txt").readlines())),
    input_2 := input_1.copy(),
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
    find(0, input_1, "most"),
    find(0, input_2, "least")
)
