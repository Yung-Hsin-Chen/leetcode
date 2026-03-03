# Problem

Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

Return `true` if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return `false` otherwise.

Example 1:

<img src="../../images/1496-1.png" alt="Example_1" width="40%">

> **Input:** path = "NES"\
> **Output:** false \
> **Explanation:** Notice that the path doesn't cross any point more than once.

Example 2:

<img src="../../images/1496-2.png" alt="Example_1" width="40%">

> **Input:** path = "NESWW"\
> **Output:** true\
> **Explanation:** Notice that the path visits the origin twice.

Constraints:

- `1 <= path.length <= 104`
- `path[i]` is either `'N'`, `'S'`, `'E'`, or `'W'`.

# Solution

The goal is to determine whether the path ever returns to a position that has already been visited. If at any step we reach a coordinate that we have seen before, the path crosses itself.

We begin at the origin `(0, 0)`. A dictionary direction maps each character (`'N'`, `'S'`, `'E'`, `'W'`) to its corresponding movement on the 2D plane.

We maintain a set called passed to store all previously visited coordinates. Since sets provide constant-time lookups on average, they allow us to efficiently check whether a position has already been visited.

Initially, we add `(0, 0)` to the set because we start there. Then, for each direction in path, we update the current position by adding the appropriate movement vector. After computing the new position, we check whether it is already in passed:
- If it is, we immediately return `True` because we have revisited a location.
- Otherwise, we add the new position to the set and continue.

If we finish processing the entire path without revisiting any coordinate, we return `False`.

Complexity:
- **Time Complexity:** O(n) because we process each character in the path once.
- **Space Complexity:** O(n) because in the worst case we may store up to n + 1 distinct coordinates.