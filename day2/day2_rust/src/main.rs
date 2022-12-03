use std::{fs, io};

fn get_input() -> io::Result<Vec<Vec<String>>> {
    let content = fs::read_to_string("input.txt")?;
    Ok(content
        .split('\n')
        .map(|s| s.split_whitespace().map(str::to_owned).collect())
        .collect())
}

fn points_for_shape(shape: &str) -> u32 {
    match shape {
        "A" => 1,
        "X" => 1,
        "B" => 2,
        "Y" => 2,
        "C" => 3,
        "Z" => 3,
        _ => unimplemented!("yeah we shouldn't get here"),
    }
}

fn result(shape_1: u32, shape_2: u32) -> u32 {
    if shape_1 == shape_2 {
        return shape_2 + 3;
    }

    shape_2
        + match (shape_1, shape_2) {
            (1, 2) => 6,
            (1, 3) => 0,
            (2, 1) => 0,
            (2, 3) => 6,
            (3, 1) => 6,
            (3, 2) => 0,
            _ => unreachable!("yeah we shouldn't get here"),
        }
}

fn result_for_shape(shape_1: &str, shape_2: &str) -> u32 {
    match (shape_1, shape_2) {
        ("A", "X") => 3,
        ("A", "Y") => 4,
        ("A", "Z") => 8,
        ("B", "X") => 1,
        ("B", "Y") => 5,
        ("B", "Z") => 9,
        ("C", "X") => 2,
        ("C", "Y") => 6,
        ("C", "Z") => 7,
        _ => unreachable!("yeah we shouldn't get here"),
    }
}

fn part_1(input: &[Vec<String>]) {
    let sum: u32 = input
        .iter()
        .map(|r| (points_for_shape(&r[0]), points_for_shape(&r[1])))
        .map(|(s1, s2)| result(s1, s2))
        .sum();

    println!("{sum}");
}

fn part_2(input: &[Vec<String>]) {
    let sum: u32 = input.iter().map(|r| result_for_shape(&r[0], &r[1])).sum();

    println!("{sum}");
}

fn main() -> io::Result<()> {
    let input = get_input()?;
    part_1(&input);
    part_2(&input);

    Ok(())
}
