# A* Search – 8 Puzzle

## Aim

To implement the A* Search algorithm for solving the 8 Puzzle problem.

## Algorithm

A* Search selects the state with the lowest estimated total cost.

### Evaluation Function

```text
f(n) = g(n) + h(n)
```

Where:

* `g(n)` = cost from the initial state
* `h(n)` = heuristic cost to the goal

The program uses the number of misplaced tiles as the heuristic.

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
python astar.py
```

## Expected Output

The program displays the sequence of puzzle states and finally prints:

```text
Goal Reached!
```

## Result

Thus, the A* Search algorithm was successfully implemented for solving the 8 Puzzle problem.
