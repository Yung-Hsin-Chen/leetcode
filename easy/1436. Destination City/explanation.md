# Problem

You are given the array `paths`, where `paths[i] = [cityA_i, cityB_i]` means there exists a direct path going from `cityA_i` to `cityB_i`. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

> Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]\
> Output: "Sao Paulo" \
> Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
> 
Example 2:

> Input: paths = [["B","C"],["D","B"],["C","A"]]\
> Output: "A"\
> Explanation: All possible trips are: \
> "D" -> "B" -> "C" -> "A". \
> "B" -> "C" -> "A". \
> "C" -> "A". \
> "A". \
> Clearly the destination city is "A".

Example 3:

> Input: paths = [["A","Z"]]\
> Output: "Z"
 

Constraints:

- `1 <= paths.length <= 100
paths[i].length == 2`
- `1 <= cityA_i.length, cityB_i.length <= 10
cityA_i != cityB_i`
- All strings consist of lowercase and uppercase English letters and the space character.

# Solution

The goal is to find the destination city, which is the city that has no outgoing path. Since the problem guarantees the paths form a line without loops, there will be exactly one such city.

The key observation is that:
- Every starting city appears as a source (cityA).
- The destination city appears only as a destination (cityB) and never as a source.

The solution uses two sets:
- outgoing stores all cities that appear as starting points.
- ingoing stores all cities that appear as destinations.

We iterate through paths and add:
- path[0] to the outgoing set.
- path[1] to the ingoing set.

At the end, the destination city is the one that appears in ingoing but not in outgoing. Since the graph forms a single line without loops, this difference will contain exactly one city.

We compute ingoing - outgoing and return the only element in that set.

Complexity:
- **Time Complexity:** O(n) because we iterate through the list of paths once.
- **Space Complexity:** O(n) because we store cities in two sets.