# Greedy Best-First Search – 8 Puzzle

## Aim

To implement the Greedy Best-First Search algorithm for solving the 8 Puzzle problem.

## Algorithm

Greedy Best-First Search selects the state that appears closest to the goal using a heuristic function.

### Evaluation Function

```text
f(n) = h(n)
```

Where `h(n)` represents the number of misplaced tiles.

## Problem Used

The 8 Puzzle consists of 8 numbered tiles and one blank space. The objective is to reach:

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
python greedy_bfs.py
```

## Expected Output

The program displays the puzzle states explored by the algorithm and prints:

```text
Goal Reached!
```

## Result

Thus, the Greedy Best-First Search algorithm was successfully implemented for the 8 Puzzle problem.
