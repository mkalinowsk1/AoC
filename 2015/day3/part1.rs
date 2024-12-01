use std::fs;
use std::io::prelude::*;
use std::collections::HashSet;

fn main() -> std::io::Result<()> {
	let mut input = fs::File::open("input.in")?;
	let mut data = String::new();
	input.read_to_string(&mut data)?;
	
	let mut point = (0, 0);
	let mut visited = HashSet::new();
	visited.insert(point);

	for char in data.chars() {
		match char {
			'^' => point.1 += 1,
			'v' => point.1 -= 1,
			'>' => point.0 += 1,
			'<' => point.0 -= 1,
			_ => {}
		}
		visited.insert(point);
	}
	println!("{}", visited.len());

	Ok(())


}