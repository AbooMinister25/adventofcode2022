import argparse
import pathlib
import subprocess

PYTHON_FILE_TEMPLATE = """import more_itertools
from aoc_lube import fetch, submit


def part_1() -> None:
    ...


def part_2() -> None:
    ...


if __name__ == "__main__":
    raw_input = fetch(2022, 3)
"""


parser = argparse.ArgumentParser("generator", description="Generates the structure for a solution.")
parser.add_argument("day", type=int)


def install_python_deps(cwd: pathlib.Path) -> None:
    # Required Dependencies
    subprocess.run(["pdm", "add", "aoc-lube[utils]"], cwd=cwd)
    subprocess.run(["pdm", "add", "more-itertools"], cwd=cwd)
    # Development Dependencies
    subprocess.run(["pdm", "add", "-dG", "format", "black"], cwd=cwd)
    subprocess.run(["pdm", "add", "-dG", "format", "isort"], cwd=cwd)
    subprocess.run(["pdm", "add", "-dG", "lint", "flake8"], cwd=cwd)
    subprocess.run(["pdm", "add", "-dG", "repl", "ipython"], cwd=cwd)


def generate(day: int) -> None:
    print("Generating Files")

    path = pathlib.Path(f"day{day}")
    path.mkdir(parents=True, exist_ok=True)

    rust_path = path / f"day{day}_rust"
    python_path = path / f"day{day}_python"

    rust_path.mkdir(parents=True, exist_ok=True)
    python_path.mkdir(parents=True, exist_ok=True)

    # Initialize rust and python projects
    subprocess.run(["cargo", "init"], cwd=rust_path)
    subprocess.run(["pdm", "init"], cwd=python_path)

    # Install dependencies for python project
    subprocess.run(["pdm", "add", "black"])

    python_src_path = python_path / "src"
    python_src_path.mkdir(parents=True, exist_ok=True)
    python_file_path = python_src_path / "main.py"

    # Write to the python file
    with open(python_file_path, "w+") as f:
        f.write(PYTHON_FILE_TEMPLATE.format(day=day))


if __name__ == "__main__":
    args = parser.parse_args()
    generate(args.day)
