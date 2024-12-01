from collections import defaultdict
import operator

# Function to read the graph from the input file
def read_graph(fname):
    graph = defaultdict(list)
    with open(fname) as filep:
        for line in filep.readlines():
            split = line.split()
            if len(split) == 3:  # Direct assignment
                graph[split[-1]] = ["EQ", split[0]]
            elif len(split) == 4:  # Unary operation (e.g., NOT)
                graph[split[-1]] = ["NOT", split[1]]
            else:  # Binary operations (e.g., AND, OR)
                graph[split[-1]] = (split[1], split[0], split[2])
    return graph

# Operation functions for bitwise operations
def op_eq(value):
    return value

def op_not(value):
    return ~value & 0xffff

# Dictionary mapping operations to their corresponding functions
OPERATIONS = {
    "EQ": op_eq,
    "NOT": op_not,
    "AND": operator.iand,
    "OR": operator.ior,
    "RSHIFT": operator.rshift,
    "LSHIFT": operator.lshift
}

# Memoization class to cache results of evaluations
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, graph, key):
        if key not in self.memo:
            self.memo[key] = self.f(graph, key)
        return self.memo[key]

    def clear(self):
        self.memo.clear()

# Function to evaluate wire values
@Memoize
def evaluate_wire(graph, key):
    try:
        return int(key)  # Direct number
    except ValueError:
        pass  # Not a direct number, continue to evaluate

    value = graph[key]
    op = value[0]

    if len(value) == 2:  # Unary operations (e.g., NOT)
        return OPERATIONS[op](evaluate_wire(graph, value[1]))
    else:  # Binary operations (e.g., AND, OR)
        return OPERATIONS[op](evaluate_wire(graph, value[1]), evaluate_wire(graph, value[2]))

# Main function
def main():
    graph = read_graph("input.in")
    
    # Step 1: Get the signal on wire a
    signal_a = evaluate_wire(graph, "a")

    # Step 2: Override wire b with the signal from wire a
    graph["b"] = ["EQ", str(signal_a)]

    # Step 3: Clear the memoization cache for fresh calculations
    evaluate_wire.memo.clear()
    
    # Step 4: Now evaluate again without resetting to 0
    # Instead of resetting wires to 0, we just clear the cache and re-evaluate wire a
    new_signal_a = evaluate_wire(graph, "a")
    
    print(f"The new signal on wire a is: {new_signal_a}")

if __name__ == "__main__":
    main()
