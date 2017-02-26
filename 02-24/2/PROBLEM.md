# Problem statement

Taylor feels exceptionally lazy and the thought of taking the stairs is too much of a burden. In fact, even walking too far to an elevator sounds painful.

Given Taylor's current position in (x,y) coordinates and coordinates of some elevators, tell Taylor which elevator he should move to in order to avoid exerting himself.

Note that because of Taylor's exceptional laziness, he can only move in the four cardinal directions.

If there are no elevators available, tell Taylor to move to the origin (where he will proceed to rethink his life). If he is standing at an elevator already, tell him to stay where he is.

There will be no ties.

# Input format

The input will start with a number T, the number of test cases.

Each test case starts with a line containing two space-separated integers, X and Y, Taylor's starting location.

The next line contains a single integer E, the number of elevators. E lines of space-separated X and Y coordinates follow.

# Constraints

$ 1 \leq T \leq 10 $

$ -10,000 \leq X,Y \leq 10,000 $

$ 0 \leq E \leq 10,000 $

# Output format

Output the coordinate to which Taylor should move in `(X,Y)` format. For example, output the origin as:

`(0,0)`