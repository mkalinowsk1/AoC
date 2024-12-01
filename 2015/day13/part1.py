from itertools import permutations
from typing import List, Tuple

def parse_input(file: str) -> List[Tuple[str, str, int]]:
    relations = []
    with open(file) as f:
        for line in f:
            parts = line.strip().split()
            person1 = parts[0]
            person2 = parts[-1].strip('.')
            happiness_change = int(parts[3])
            if parts[2] == "lose":
                happiness_change = -happiness_change
            relations.append((person1, person2, happiness_change))
    return relations

def build_happiness_map(relations: List[Tuple[str, str, int]]) -> dict:
    happiness_map = {}
    for person1, person2, change in relations:
        if person1 not in happiness_map:
            happiness_map[person1] = {}
        happiness_map[person1][person2] = change
    return happiness_map

def calculate_happiness(arrangement: List[str], happiness_map: dict) -> int:
    total_happiness = 0
    n = len(arrangement)
    for i in range(n):
        person1 = arrangement[i]
        person2 = arrangement[(i + 1) % n]  # Next person in the circular seating
        total_happiness += happiness_map[person1][person2]
        total_happiness += happiness_map[person2][person1]
    return total_happiness

def find_optimal_seating(happiness_map: dict) -> Tuple[List[str], int]:
    people = list(happiness_map.keys())
    max_happiness = float('-inf')
    best_arrangement = None

    # Generate all permutations of seating arrangements
    for arrangement in permutations(people):
        happiness = calculate_happiness(arrangement, happiness_map)
        if happiness > max_happiness:
            max_happiness = happiness
            best_arrangement = arrangement

    return best_arrangement, max_happiness

# Parse input and build the happiness map
relations = parse_input('input.in')
happiness_map = build_happiness_map(relations)

# Find the optimal seating arrangement
best_arrangement, max_happiness = find_optimal_seating(happiness_map)

# Print the results
print("Optimal seating arrangement:", " -> ".join(best_arrangement))
print("Total happiness:", max_happiness)
