graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start = 'A'
goal = 'G'

stack = [[start]]
visited = set()

while stack:
    path = stack.pop()
    node = path[-1]

    if node == goal:
        print("DFS Path:", path)
        break

    if node not in visited:
        visited.add(node)

        for neighbor in reversed(graph[node]):
            stack.append(path + [neighbor])