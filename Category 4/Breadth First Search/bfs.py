from collections import deque

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

queue = deque([[start]])
visited = set()

while queue:
    path = queue.popleft()
    node = path[-1]

    if node == goal:
        print("BFS Path:", path)
        break

    if node not in visited:
        visited.add(node)

        for neighbor in graph[node]:
            new_path = path + [neighbor]
            queue.append(new_path)