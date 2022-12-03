use std::cmp::Reverse;
use std::{fs, io};

fn get_input() -> io::Result<Vec<String>> {
    let content = fs::read_to_string("input.txt")?;
    Ok(content.split("\n\n").map(str::to_owned).collect())
}

fn part_1(input: Vec<String>) -> Vec<u32> {
    let mut summed = input
        .iter()
        .map(|s| {
            s.split('\n')
                .filter(|n| !n.is_empty())
                .map(|n| n.parse::<u32>().unwrap())
                .collect::<Vec<u32>>()
        })
        .map(|s| s.iter().sum())
        .collect::<Vec<u32>>();

    summed.sort_by_key(|n| Reverse(*n));

    summed
}

fn main() -> io::Result<()> {
    let input = get_input()?;
    let summed = part_1(input);

    println!("{}", summed[0]);

    // Part 2
    let sum: u32 = summed[0..3].iter().sum();
    println!("{}", sum);

    Ok(())
}
