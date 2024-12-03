(
    lambda directions, _:
        print(directions["forward"] * (directions["down"] - directions["up"]))
)(
    commands := {"up": 0, "down": 0, "forward": 0},
    [
        commands.__setitem__(
            command,
            commands[command] + int(amount)
        ) for command, amount in list(map(str.split, open("input.txt").readlines()))
    ]
)
