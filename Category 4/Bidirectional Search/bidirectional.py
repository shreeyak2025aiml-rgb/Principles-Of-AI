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

reverse_graph = {
    'A': [],
    'B': ['A'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['E', 'F']
}

start = 'A'
goal = 'G'

front_start = {start: [start]}
front_goal = {goal: [goal]}

queue_start = deque([start])
queue_goal = deque([goal])

meeting = None

while queue_start and queue_goal:

    current = queue_start.popleft()

    for neighbor in graph[current]:
        if neighbor not in front_start:
            front_start[neighbor] = front_start[current] + [neighbor]
            queue_start.append(neighbor)

            if neighbor in front_goal:
                meeting = neighbor
                break

    if meeting:
        break

    current = queue_goal.popleft()

    for neighbor in reverse_graph[current]:
        if neighbor not in front_goal:
            front_goal[neighbor] = [neighbor] + front_goal[current]
            queue_goal.append(neighbor)

            if neighbor in front_start:
                meeting = neighbor
                break

    if meeting:
        break

if meeting:
    path = front_start[meeting][:-1] + front_goal[meeting]
    print("Bidirectional Path:", path)
else:
    print("Path not found")