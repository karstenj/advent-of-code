use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::vec::Vec;

fn main() {
    get_solution_part1("../input1.txt");
    get_solution_part1("../input2.txt");
    get_solution_part2("../input1.txt");
    get_solution_part2("../input2.txt");
}

fn get_solution_part1(filename: &str) -> u32 {
    let vec = get_vec(filename);
    let mut result = 0;
    match vec.first() {
        Some(x) => {result = *x},
        None => {}
    }
    println!("Result {} {}", filename, result);
    return result;
}

fn get_solution_part2(filename: &str) -> u32 {
    let vec = get_vec(filename);
    let slice = &vec[0..3];
    let result = slice.iter().sum();
    println!("Result {} {}", filename, result);
    return result;
}

fn get_vec(filename: &str) -> Vec<u32> {
    let mut vec: Vec<u32> = Vec::new();
    vec.push(0);
    if let Ok(lines) = read_lines(filename) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                let value: u32 = match ip.parse() {
                    Ok(num) => num,
                    Err(_) => {
                        vec.push(0);
                        continue;
                    }
                };
                match vec.last_mut() {
                    None => {},
                    Some(x) => *x += value,
                };    
            }
        }
    }
     vec.sort_by(|a, b| b.cmp(a));
    return vec;
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution_part1() {
        assert_eq!(get_solution_part1("../input1.txt"), 24000);
        assert_eq!(get_solution_part1("../input2.txt"), 66487);
    }

    #[test]
    fn test_solution_part2() {
        assert_eq!(get_solution_part2("../input1.txt"), 45000);
        assert_eq!(get_solution_part2("../input2.txt"), 197301);
    }
}