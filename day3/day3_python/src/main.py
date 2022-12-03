import string
import functools

from aoc_lube import fetch, submit
from more_itertools import chunked


priorities = dict(zip(string.ascii_letters, range(1, 53)))


def part_1(data: list[str]) -> int:
    halves = [
        next(iter(set(i[: int(len(i) / 2)]) & set(i[int(len(i) / 2) :]))) for i in data
    ]
    priorities_sum = sum(priorities[s] for s in halves)

    return priorities_sum


def part_2(data: list[str]) -> int:
    chunks = chunked(data, 3)
    badges = [next(iter(set(a) & set(b) & set(c))) for a, b, c in chunks]
    priorities_sum = sum(priorities[s] for s in badges)

    return priorities_sum


if __name__ == "__main__":
    data = fetch(2022, 3).splitlines()
    part_1(data)

    submit(2022, 3, 1, functools.partial(part_1, data))
    submit(2022, 3, 2, functools.partial(part_2, data))
