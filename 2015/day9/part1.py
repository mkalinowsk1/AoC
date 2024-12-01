from typing import Dict, List, Tuple
from collections import defaultdict

class Graph:
    def __init__(self, edges: List[Tuple[str, str, int]]):
        self.edges = edges
        self.graph: Dict[str, Dict[str, int]] = defaultdict(dict)  # Store neighbors with weights
        self.visited = defaultdict(lambda: False)

        self.make_graph(edges)
        self.visited_nodes = 0
        self.total_nodes = len(self.graph.keys())

    def make_graph(self, _edges: List[Tuple[str, str, int]]) -> None:
        """Build the graph from the list of edges (u, v, distance)."""
        for u, v, d in _edges:
            self.graph[u][v] = d  # Store the weight (distance)
            self.graph[v][u] = d  # Since it's undirected, add both directions

    def visit(self, node: str) -> None:
        """Mark a node as visited."""
        self.visited[node] = True
        self.visited_nodes += 1

    def un_visit(self, node: str) -> None:
        """Mark a node as unvisited."""
        self.visited[node] = False
        self.visited_nodes -= 1

    def all_nodes_are_visited(self) -> bool:
        """Check if all nodes have been visited."""
        return self.visited_nodes == self.total_nodes

    def get_hamiltonian_path(self, start: str, current_distance: int = 0) -> List[Tuple[List[str], int]]:
        """Recursively find all Hamiltonian paths starting from 'start'. Track the current total distance."""
        self.visit(start)
        all_paths = []

        if self.all_nodes_are_visited():
            # If all nodes are visited, return the current path with its total distance
            all_paths.append(([start], current_distance))

        for neighbor, distance in self.graph[start].items():
            if not self.visited[neighbor]:
                # Recur for the next node and accumulate the distance
                paths = self.get_hamiltonian_path(neighbor, current_distance + distance)
                for path, dist in paths:
                    all_paths.append((path + [start], dist))  # Append 'start' to the path

        self.un_visit(start)
        return all_paths

# Parse the input file
edges = []
cities = []
with open("input.in") as fin:
    file = fin.read().splitlines()

for line in file:
    line = line.split(" ")
    cities.append(line[0])
    A = line[0]
    B = line[2]
    dist = int(line[-1])
    edges.append((A, B, dist))

# Create the graph
graph = Graph(edges)

for city in cities:
# Get all Hamiltonian paths starting from a node (e.g., "Tristram")
	hamiltonian_paths = graph.get_hamiltonian_path(start=city)

	# Find the shortest Hamiltonian path
	shortest_path = max(hamiltonian_paths, key=lambda x: x[1])  # x[1] is the total distance

	# Print the shortest path and its distance
	print("Shortest path:", " -> ".join(reversed(shortest_path[0])), "with distance:", shortest_path[1])
