# Problem

Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

Return `true` if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return `false` otherwise.

Example 1:

<img src="../../images/1496-1.png" alt="Example_1" width="60%">

> **Input:** path = "NES"\
> **Output:** false \
> **Explanation:** Notice that the path doesn't cross any point more than once.

Example 2:

<img src="../../images/1496-2.png" alt="Example_1" width="60%">

> **Input:** path = "NESWW"\
> **Output:** true\
> **Explanation:** Notice that the path visits the origin twice.

Constraints:

- `1 <= path.length <= 104`
- `path[i]` is either `'N'`, `'S'`, `'E'`, or `'W'`.
