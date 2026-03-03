# Problem

Given a **0-indexed** `n x n` integer matrix `grid`, return the number of pairs `(r_i, c_j)` such that row `r_i` and column `c_j` are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
> Input: grid = [[3,2,1],[1,7,6],[2,7,7]]\
> Output: 1\
> Explanation: There is 1 equal row and column pair:
> - (Row 2, Column 1): [2,7,7]

Example 2:
> Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]\
> Output: 3\
> Explanation: There are 3 equal row and column pairs:
> - (Row 0, Column 0): [3,1,2,2]
> - (Row 2, Column 2): [2,4,2,2]
> - (Row 3, Column 2): [2,4,2,2]
 

Constraints:

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 105`

# Solution

The goal is to count how many pairs `(r_i, c_j)` exist such that a row and a column contain exactly the same elements in the same order.

A brute-force approach would compare every row with every column directly, leading to `O(n³)` time complexity, since each comparison takes `O(n)` time. Instead, this solution reduces the repeated comparisons by using a hash map.

First, we process all rows. Since lists cannot be dictionary keys, we convert each row into a tuple and store it in a dictionary counts, where:
- The key is the row (as a tuple).
- The value is how many times that exact row appears in the grid.

Next, we construct each column. For each column index `i`, we collect elements `grid[row][i]` for all rows and form a list representing that column.

For every column we build:
- Convert it to a tuple.
- Check how many times this tuple appears in the counts dictionary.
- Add that count to the answer.

If a row appears multiple times and matches a column, each occurrence contributes to the total count, which is handled naturally by storing frequencies in counts.

By grouping rows first and then checking each column against this grouped structure, we efficiently compute the number of equal row-column pairs.

### Complexity:
- **Time Complexity:** O(n²) because we process n rows and build n columns, each of length n.
- **Space Complexity:** O(n²) for storing row tuples in the dictionary.