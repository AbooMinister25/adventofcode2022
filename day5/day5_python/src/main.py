import functools

from typing import Iterator

from aoc_lube import submit
from aoc_lube.utils import extract_ints


def read_input() -> str:
    with open("input.txt", "r") as f:
        raw = f.read()

    return raw


def parse_input(raw: str) -> tuple[list[Iterator[int]], list[list[str]]]:
    filled: list[list[str]] = []
    crate_lines = [line for line in raw.splitlines() if not line.startswith("move") and line]

    for line in crate_lines:
        filled.append(line.replace("    ", " [] ").split())

    crates: list[list[str]] = list(map(list, zip(*filled)))
    crates = [
        [
            crate.replace("[", "").replace("]", "")
            for crate in row
            if crate != "[]" and not crate.isnumeric()
        ]
        for row in crates
    ]

    instructions: list[Iterator[int]] = [
        extract_ints(l) for l in raw.splitlines() if l.startswith("move")
    ]

    return instructions, crates


def part_1(instructions: list[Iterator[int]], crates: list[list[str]]) -> str:
    for instruction in instructions:
        amount = next(instruction)
        from_ = next(instruction)
        to = next(instruction)

        for _ in range(amount):
            crates[to - 1].insert(0, (crates[from_ - 1].pop(0)))

    return "".join(crate[0] for crate in crates)


def part_2(instructions: list[Iterator[int]], crates: list[list[str]]) -> str:
    for instruction in instructions:
        amount = next(instruction)
        from_ = next(instruction)
        to = next(instruction)

        for i in reversed(range(0, amount)):
            crates[to - 1].insert(0, (crates[from_ - 1].pop(i)))

    return "".join(crate[0] for crate in crates)


if __name__ == "__main__":
    raw_input = read_input()
    instructions, crates = parse_input(raw_input)

    submit(2022, 5, 1, functools.partial(part_1, instructions, crates))
    submit(2022, 5, 2, functools.partial(part_2, instructions, crates))
