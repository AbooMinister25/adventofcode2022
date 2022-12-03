def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        content = f.read().split("\n\n")

    return content


def part_1(input_data: list[str]) -> list[int]:
    calories = [[int(n) for n in lines.split("\n") if n] for lines in input_data]
    summed = sorted([sum(i) for i in calories], reverse=True)

    return summed


if __name__ == "__main__":
    input_data = get_input()
    summed = part_1(input_data)
    print(summed[0])

    # Part 2
    print(sum(summed[:3]))
