(
    lambda _, gamma, epsilon:
        print(int("".join(gamma), 2) * int("".join(epsilon), 2))
)(
    inputs := list(map(list, map(str.strip, open("input.txt").readlines()))),
    [__import__("collections").Counter([binary[digit] for binary in inputs]).most_common()[0][0] for digit in range(12)],
    [__import__("collections").Counter([binary[digit] for binary in inputs]).most_common()[-1][0] for digit in range(12)],
)
