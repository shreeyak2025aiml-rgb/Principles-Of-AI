# Memory-Bounded Heuristic Search – 8 Puzzle

## Aim

To implement a Memory-Bounded Heuristic Search algorithm for solving the 8 Puzzle problem.

## Algorithm

The program uses **IDA*** (Iterative Deepening A*) as a memory-bounded heuristic search technique.

IDA* combines:

* Depth-first search
* A* heuristic evaluation
* Limited memory usage

### Evaluation Function

```text
f(n) = g(n) + h(n)
```

The heuristic `h(n)` is the number of misplaced tiles.

## Problem Used

The goal state is:

```text
1 2 3
4 5 6
7 8 _
```

## Requirements

* Python 3.x
* No external libraries are required.

## How to Run

```bash
python memory_bounded.py
```

## Expected Output

The program prints the solution path and displays:

```text
Solution: [...]
```

## Advantages

* Uses significantly less memory than standard A*.
* Suitable for large search spaces.
* Uses heuristic information to guide the search.

## Result

Thus, the Memory-Bounded Heuristic Search algorithm using IDA* was successfully implemented for the 8 Puzzle problem.
