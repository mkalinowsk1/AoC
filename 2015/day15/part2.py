import itertools

TOTAL = 100
INGREDIENTS = 4

class Frosting:
    capacity = 4
    durability = -2
    flavor = 0
    texture = 0
    calories = 5

class Candy:
    capacity = 0
    durability = 5
    flavor = -1
    texture = 0
    calories = 8
    
class Butterscotch:
    capacity = -1
    durability = 0
    flavor = 5
    texture = 0
    calories = 6
    
class Sugar:
    capacity = 0
    durability = 0
    flavor = -2
    texture = 2
    calories = 1
    

# Define the evaluation function
def calculate_total_sweetness(frosting, candy, butterscotch, sugar):
    # Example weights for sweetness
    cap = frosting * Frosting.capacity + candy * Candy.capacity + butterscotch * Butterscotch.capacity + sugar * Sugar.capacity
    dur = frosting * Frosting.durability + candy * Candy.durability + butterscotch * Butterscotch.durability + sugar * Sugar.durability
    fla = frosting * Frosting.flavor + candy * Candy.flavor + butterscotch * Butterscotch.flavor + sugar * Sugar.flavor
    tex = frosting * Frosting.texture + candy * Candy.texture + butterscotch * Butterscotch.texture + sugar * Sugar.texture
    cal = frosting * Frosting.calories + candy * Candy.calories + butterscotch * Butterscotch.calories + sugar * Sugar.calories
    if cap < 0:
        cap = 0
    if dur < 0:
        dur = 0
    if fla < 0:
        fla = 0
    if tex < 0:
        tex = 0
    score = cap * dur * fla * tex
    if cal != 500:
        return 0
    return score
    
        

# Function to generate combinations
def generate_combinations(total, ingredients):
    for dividers in itertools.combinations(range(total + ingredients -1), ingredients -1):
        quantities = []
        previous = -1
        for divider in dividers:
            quantities.append(divider - previous - 1)
            previous = divider
        quantities.append(total + ingredients -1 - dividers[-1] -1)
        yield quantities

# Initialize variables to track the best combination
best_combination = None
best_score = float('-inf')  # Assuming we're maximizing
best_combinations = []  # To handle multiple combinations with the same best score

# Iterate through all combinations
for combo in generate_combinations(TOTAL, INGREDIENTS):
    frosting, candy, butterscotch, sugar = combo
    # Perform your calculation
    score = calculate_total_sweetness(frosting, candy, butterscotch, sugar)
    
    # Update best combination(s) if necessary
    if score > best_score:
        best_score = score
        best_combination = combo
        best_combinations = [combo]  # Reset the list
    elif score == best_score:
        best_combinations.append(combo)  # Add to the list

# Output the results
print(f"Best Total Sweetness: {best_score}")
print("Best Combination(s):")
for combo in best_combinations:
    frosting, candy, butterscotch, sugar = combo
    print(f"Frosting: {frosting}, Candy: {candy}, Butterscotch: {butterscotch}, Sugar: {sugar}")
