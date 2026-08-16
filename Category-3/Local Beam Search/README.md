# Local Beam Search

## Aim

To implement the **Local Beam Search algorithm** for solving a state search space optimization problem.

## Concept

Local Beam Search maintains multiple candidate states instead of working with only one state.

If `k = 3`, the algorithm keeps the three best states at every iteration.

This allows the algorithm to explore multiple paths simultaneously.

## Use Case

A robot searches a grid where every cell contains a reward value. Multiple possible positions are maintained during the search to find a high-reward state.

## Algorithm

1. Generate `k` random initial states.
2. Generate neighbouring states for each current state.
3. Combine all current and neighbouring states.
4. Evaluate their values.
5. Select the best `k` states.
6. Repeat for a fixed number of iterations.
7. Select the best state from the final states.

## Example

For:

```text
k = 3
```

the algorithm maintains three candidate states:

```text
State 1 → Neighbours
State 2 → Neighbours
State 3 → Neighbours
          ↓
   Select best 3
          ↓
      Next iteration
```

## Advantages

* Searches multiple paths simultaneously.
* Provides more exploration than basic Hill Climbing.
* Can reduce the chance of getting trapped in a poor local optimum.

## Limitations

* Requires more memory than Hill Climbing.
* Multiple states increase computational cost.
* Different states may converge to the same region.

## Technologies

* Python 3
* Random module

## How to Run

```bash
python local_beam_search.py
```

## Expected Output

```text
Iteration 1
(2, 2) Value: 9
(1, 3) Value: 8
(3, 2) Value: 8

...

Local Beam Search Result
Best State: (2, 2)
Best Value: 9
```

## Conclusion

Local Beam Search improves exploration by maintaining multiple candidate states. It is useful for state-space problems where exploring several promising paths can produce better results than following a single path.
