# Depth Limited Search

## Aim

To implement the **Depth Limited Search (DLS)** uninformed search technique with a predefined depth limit.

## Use Case

An AI robot searches for a destination but is allowed to explore only up to a specific number of steps. This prevents the search from going indefinitely deep.

## Concept

Depth Limited Search is a modified version of DFS.

The main difference is that DLS has a **maximum depth limit**.

For example:

```text
Depth 0 → A

Depth 1 → B, C

Depth 2 → D, E, F

Depth 3 → G
```

If the goal is beyond the specified depth limit, it will not be reached.

## Algorithm

1. Start from the initial node.
2. Set a maximum depth limit.
3. Visit the current node.
4. Check whether it is the goal.
5. If the depth limit is reached, stop exploring that branch.
6. Otherwise, recursively explore its neighbours.
7. Continue until the goal is found or all permitted states are explored.

## Important Parameter

```text
Depth Limit = 3
```

The algorithm cannot explore states beyond depth 3.

## Advantages

* Prevents infinite depth exploration.
* Uses less memory.
* Useful when the expected solution depth is known.

## Disadvantages

* May fail if the goal is deeper than the limit.
* Does not guarantee the shortest path.
* Choosing a suitable depth limit can be difficult.

## How to Run

```bash
python dls.py
```

## Expected Output

```text
DLS Path: ['A', 'B', 'E', 'G']
```

## Conclusion

DLS combines the depth-first strategy with a depth limit. It is useful when the search should be restricted to a known maximum depth.
