# Depth First Search to find path between two nodes

adj_list = {
    "a": ["b", "d"],
    "b": ["a", "c"],
    "c": ["b"],
    "d": ["a", "e", "f"],
    "e": ["d", "f", "g"],
    "f": ["d", "e", "h"],
    "g": ["e", "h"],
    "h": ["f", "g"]
}

visited = {}
parent = {}

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None

dfs_output = []

# Recursive DFS function
def dfs(node):
    visited[node] = True
    dfs_output.append(node)
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            parent[neighbour] = node
            dfs(neighbour)

# User input for source and destination
source = input("Enter source node: ").lower()
destination = input("Enter destination node: ").lower()

# Perform DFS
dfs(source)

print("\nDFS Traversal:", dfs_output)

# Reconstruct the path from source to destination
path = []
if visited[destination]:
    while destination is not None:
        path.append(destination)
        destination = parent[destination]
    path.reverse()
    print("Path from source to destination:", " → ".join(path))
else:
    print("No path found between the given nodes.")
