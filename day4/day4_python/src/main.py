import functools
from typing import Iterator

from aoc_lube import fetch, submit
from aoc_lube.utils import extract_ints


def part_1(ranges: list[Iterator[int]]) -> int:
    r = [
        i
        for i in ranges
        if (a := set(range(next(i), next(i) + 1))).issubset(
            b := set(range(next(i), next(i) + 1))
        )
        or b.issubset(a)
    ]

    return len(r)


def part_2(ranges: list[Iterator[int]]) -> int:
    r = [
        i
        for i in ranges
        if set(range(next(i), next(i) + 1)) & set(range(next(i), next(i) + 1))
    ]

    return len(r)


if __name__ == "__main__":
    raw_input = fetch(2022, 4).splitlines()
    ranges = [map(abs, extract_ints(l)) for l in raw_input]

    submit(2022, 4, 1, functools.partial(part_1, ranges))
    submit(2022, 4, 2, functools.partial(part_2, ranges))
