# Simulated Annealing Search

## Aim

To implement the **Simulated Annealing Search algorithm** for solving a state search space optimization problem.

## Concept

Simulated Annealing is a local search algorithm inspired by the cooling process of metals.

Unlike Hill Climbing, it can accept a worse state temporarily. This helps the algorithm escape from local optima.

The probability of accepting a worse state is calculated using:

```text
P = e^(-ΔE / T)
```

where:

* `P` = probability of accepting the worse state
* `ΔE` = difference between the current and next state
* `T` = current temperature

## Use Case

A robot searches a grid where every cell represents a reward. The objective is to find a state with the highest possible reward.

## Algorithm

1. Start with an initial state.
2. Set a high temperature.
3. Select a random neighbouring state.
4. If the new state is better, accept it.
5. If the new state is worse, accept it with a probability based on temperature.
6. Gradually reduce the temperature.
7. Continue until the temperature becomes very low.
8. Store and display the best state found.

## Advantages

* Can escape local optima.
* Provides better exploration at high temperatures.
* Gradually changes from exploration to exploitation.

## Technologies

* Python 3
* Random module
* Math module

## How to Run

```bash
python simulated_annealing.py
```

## Expected Output

```text
Simulated Annealing Result
Best State: (2, 2)
Best Value: 9
```

## Conclusion

Simulated Annealing provides a better chance of reaching the global optimum because it can temporarily accept worse solutions during the exploration phase.
