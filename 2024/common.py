__all__ = ["input_lines", "input_line"]

def input_lines() -> list[str]:
    return open("input.txt").readlines()

def input_line() -> str:
    return open("input.txt").read()
