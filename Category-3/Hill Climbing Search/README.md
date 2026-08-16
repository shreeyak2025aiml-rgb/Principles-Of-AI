# Hill Climbing Search

## Aim

To implement the **Hill Climbing Search algorithm** for solving a state search space optimization problem.

## Concept

Hill Climbing is a local search algorithm that continuously moves from the current state to a better neighbouring state.

It tries to maximize the value of the current state.

## Use Case

A robot is moving through a grid where each cell contains a reward value. The robot starts at the top-left corner and attempts to reach a state with maximum reward.

## Algorithm

1. Start from an initial state.
2. Generate all neighbouring states.
3. Find the neighbour with the highest value.
4. Move to the neighbour if its value is greater than the current state.
5. If no better neighbour exists, stop the search.
6. Display the final state and maximum value.

## Problem

Hill Climbing can get stuck in a **local optimum**.

It does not always guarantee finding the global optimum.

### Types of Problems

* Local Maximum
* Plateau
* Ridge

## Technologies

* Python 3

## How to Run

```bash
python hill_climbing.py
```

## Expected Output

```text
Current: (0, 0) Value: 1
Current: (0, 1) Value: 2
Current: (0, 2) Value: 3
...

Hill Climbing Result
State: (2, 2)
Maximum Value: 9
```

## Conclusion

Hill Climbing is simple and efficient because it only considers neighbouring states. However, it may terminate at a local optimum instead of the global optimum.
