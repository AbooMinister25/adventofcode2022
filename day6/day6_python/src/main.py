from functools import partial
from more_itertools import windowed
from aoc_lube import fetch, submit


def part_1(raw_input: str) -> int:
    return (
        raw_input.index(
            "".join([i for i in windowed(raw_input, 4) if len(set(i)) == 4][0])
        )
        + 4
    )


def part_2(raw_input: str) -> int:
    return (
        raw_input.index(
            "".join([i for i in windowed(raw_input, 14) if len(set(i)) == 14][0])
        )
        + 14
    )


if __name__ == "__main__":
    raw_input = fetch(2022, 6)

    submit(2022, 6, 1, partial(part_1, raw_input))
    submit(2022, 6, 2, partial(part_2, raw_input))
