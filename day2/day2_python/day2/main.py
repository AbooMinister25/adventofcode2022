def get_input() -> list[list[str]]:
    with open("input.txt", "r") as f:
        raw = f.read()

    return [l.split() for l in raw.splitlines()]


def win(shape_1: int, shape_2: int) -> int:
    if shape_1 == shape_2:
        return shape_2 + 3

    match (shape_1, shape_2):
        case (1, 2) | (2, 3) | (3, 1):
            return shape_2 + 6
        case (1, 3) | (2, 1) | (3, 2):
            return shape_2
        case _:
            raise ValueError("brok")  # we shouldn't really get here


def points_for_shape(shape_1: str, shape_2: str) -> int:
    match (shape_1, shape_2):
        case ("A", "X"):
            return 3
        case ("A", "Y"):
            return 4
        case ("A", "Z"):
            return 8
        case ("B", "X"):
            return 1
        case ("B", "Y"):
            return 5
        case ("B", "Z"):
            return 9
        case ("C", "X"):
            return 2
        case ("C", "Y"):
            return 6
        case ("C", "Z"):
            return 7
        case _:
            raise ValueError("brok")  # we shouldn't really get here


def part_1(data: list[list[str]]) -> None:
    point_map = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}

    points = [(point_map[a], point_map[b]) for a, b in data]
    score = sum(win(a, b) for a, b in points)

    print(score)


def part_2(data: list[list[str]]) -> None:
    score = sum([points_for_shape(a, b) for a, b in data])
    print(score)


if __name__ == "__main__":
    data = get_input()
    part_1(data)
    part_2(data)
