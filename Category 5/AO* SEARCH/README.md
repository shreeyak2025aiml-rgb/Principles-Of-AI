# AO* Search – AND-OR Graph

## Aim

To implement the AO* Search algorithm for finding the minimum-cost solution in an AND-OR graph.

## Algorithm

AO* Search works on AND-OR graphs and selects the solution with minimum estimated cost.

* **OR node:** Choose one alternative.
* **AND node:** All child nodes must be solved.

## Problem Used

A simple AND-OR graph is represented using a Python dictionary. Each node contains one or more possible sets of child nodes.

## Requirements

* Python 3.x
* No external libraries are required.

## How to Run

```bash
python ao_star.py
```

## Expected Output

The program displays the calculated cost of each node and finally prints:

```text
Minimum Cost: ...
```

## Result

Thus, the AO* Search algorithm was successfully implemented for finding the minimum-cost solution in an AND-OR graph.
