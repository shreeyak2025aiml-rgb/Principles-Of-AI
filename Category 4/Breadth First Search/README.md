# Breadth First Search

## Aim

To implement the **Breadth First Search (BFS)** uninformed search technique for finding a path between two states.

## Use Case

An AI robot needs to find a path from a starting location to a destination. The environment is represented as a graph where nodes represent locations and edges represent possible movements.

## Concept

Breadth First Search explores the search space **level by level**.

It uses a **Queue (FIFO)** data structure.

```text
A
├── B
│   ├── D
│   └── E
└── C
    └── F
```

BFS explores:

```text
A → B → C → D → E → F → G
```

## Algorithm

1. Start from the initial node.
2. Add the initial node to a queue.
3. Remove the first node from the queue.
4. Check whether it is the goal.
5. Add its unvisited neighbours to the queue.
6. Repeat until the goal is found or the queue becomes empty.
7. Display the path.

## Data Structure

**Queue (FIFO)**

## Advantages

* Complete for finite branching spaces.
* Finds the shortest path when all edges have equal cost.
* Simple to implement.

## Disadvantages

* Requires large memory.
* Can be slow for large search spaces.

## How to Run

```bash
python bfs.py
```

## Expected Output

```text
BFS Path: ['A', 'B', 'E', 'G']
```

## Conclusion

BFS systematically explores all nodes at the current depth before moving to the next depth. It is useful when the shortest path is required in an unweighted search space.
