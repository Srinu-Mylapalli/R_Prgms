from queue import PriorityQueue

# Best First Search Algorithm
def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))   # (h(n), node)

    while not pq.empty():
        h, current = pq.get()
        print("Visiting:", current)

        if current == goal:
            print("Goal reached!")
            return

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor))


# Graph representation
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F':['G'],
    'G': []
}

# Heuristic values (h)
heuristics = {
    'S': 8,
    'A': 4,
    'B': 5,
    'C': 3,
    'D': 2,
    'E': 4,
    'F':1,
    'G': 0
}

# Calling the Best First Search
best_first_search(graph, heuristics, 'S', 'G')
