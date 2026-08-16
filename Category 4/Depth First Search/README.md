# Depth First Search

## Aim

To implement the **Depth First Search (DFS)** uninformed search technique for finding a path between two states.

## Use Case

An AI robot searches through a network of connected locations to reach a destination. DFS explores one possible route as deeply as possible before backtracking.

## Concept

Depth First Search explores a branch **as deeply as possible** before moving to another branch.

It uses a **Stack (LIFO)** data structure.

```text
A
├── B
│   ├── D
│   └── E
└── C
    └── F
```

DFS explores one branch before returning and exploring another.

## Algorithm

1. Start from the initial node.
2. Push the initial node/path onto a stack.
3. Remove the top element from the stack.
4. Check whether it is the goal.
5. Add unvisited neighbours to the stack.
6. Continue until the goal is found or the stack becomes empty.
7. Display the path.

## Data Structure

**Stack (LIFO)**

## Advantages

* Requires less memory than BFS in many cases.
* Simple to implement.
* Useful for exploring deep search spaces.

## Disadvantages

* Does not guarantee the shortest path.
* Can get stuck exploring a deep branch.
* May not terminate in infinite search spaces without proper handling.

## How to Run

```bash
python dfs.py
```

## Expected Output

```text
DFS Path: ['A', 'B', 'E', 'G']
```

## Conclusion

DFS explores a search space by going deep into one branch before backtracking. It is useful when memory is limited and the shortest path is not the primary requirement.
