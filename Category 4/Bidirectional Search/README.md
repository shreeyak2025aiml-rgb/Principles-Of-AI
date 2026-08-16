# Bidirectional Search

## Aim

To implement the **Bidirectional Search** uninformed search technique for finding a path between an initial state and a goal state.

## Use Case

An AI navigation system needs to find a path between two locations. Instead of searching only from the starting point, the algorithm searches simultaneously from both the start and goal.

## Concept

Bidirectional Search performs two searches:

```text
Start → → → Meeting Point ← ← ← Goal
```

One search starts from the initial state and another starts from the goal state.

The searches continue until they meet at a common state.

## Algorithm

1. Start a search from the initial node.
2. Start another search from the goal node.
3. Expand nodes from both directions.
4. Keep track of visited states.
5. Check whether the two searches meet.
6. If they meet, combine the two paths.
7. Display the complete path.

## Example

```text
A → B → E → G
```

Forward search:

```text
A → B → E
```

Backward search:

```text
G → E
```

Meeting point:

```text
E
```

Final path:

```text
A → B → E → G
```

## Advantages

* Can be significantly faster than searching entirely from one side.
* Reduces the effective search depth.
* Useful when both start and goal states are known.

## Disadvantages

* Requires the goal state to be known.
* Requires additional memory for two searches.
* More difficult to implement than BFS or DFS.

## How to Run

```bash
python bidirectional.py
```

## Expected Output

```text
Bidirectional Path: ['A', 'B', 'E', 'G']
```

## Conclusion

Bidirectional Search reduces the search space by searching simultaneously from the start and goal states. It is particularly useful for finding paths in large, unweighted state spaces.
