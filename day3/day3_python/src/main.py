import string
import functools

from aoc_lube import fetch, submit
from more_itertools import chunked, divide


priorities = dict(zip(string.ascii_letters, range(1, 53)))


def part_1(data: list[str]) -> int:
    priorities_sum = sum(
        priorities[(set(a) & set(b)).pop()] for a, b in [divide(2, i) for i in data]
    )

    return priorities_sum


def part_2(data: list[str]) -> int:
    priorities_sum = sum(
        priorities[(set(a) & set(b) & set(c)).pop()] for a, b, c in chunked(data, 3)
    )

    return priorities_sum


if __name__ == "__main__":
    data = fetch(2022, 3).splitlines()
    part_1(data)

    print(part_1(data))
    print(part_2(data))
