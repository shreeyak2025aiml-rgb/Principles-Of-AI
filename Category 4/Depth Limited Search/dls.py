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
limit = 3

def dls(node, path, depth):

    if node == goal:
        return path

    if depth == 0:
        return None

    for neighbor in graph[node]:

        if neighbor not in path:
            result = dls(
                neighbor,
                path + [neighbor],
                depth - 1
            )

            if result:
                return result

    return None


result = dls(start, [start], limit)

if result:
    print("DLS Path:", result)
else:
    print("Goal not found within depth limit")