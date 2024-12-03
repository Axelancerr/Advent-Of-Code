(
    lambda directions, _:
        print(directions["horizontal"] * directions["depth"])
)(
    commands := {"aim": 0, "horizontal": 0, "depth": 0},
    [
        (
            commands.__setitem__("horizontal", commands["horizontal"] + int(amount)),
            commands.__setitem__("depth", commands["depth"] + (commands["aim"] * int(amount)))
        ) if command == "forward"
        else (
            commands.__setitem__("aim", commands["aim"] + int(amount))
        ) if command == "down"
        else (
            commands.__setitem__("aim", commands["aim"] - int(amount))
        ) if command == "up"
        else (
            None
        )
        for command, amount in list(map(str.split, open("input.txt").readlines()))
    ]
)
