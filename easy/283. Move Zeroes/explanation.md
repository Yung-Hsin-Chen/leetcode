# Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

> **Input:** nums = [0,1,0,3,12]\
> **Output:** [1,3,12,0,0]

Example 2:

> **Input:** nums = [0]\
> **Output:** [0]
 

Constraints:

- `1 <= nums.length <= 104`
- `-231 <= nums[i] <= 231 - 1`
 

**Follow up:** Could you minimize the total number of operations done?

# Solution

The goal is to move all zeroes to the end of the array while keeping every non-zero number in its original relative order. Because the modification must happen in-place, the solution must reuse the existing array without creating a copy.

Imagine two pointers sweeping through the array:
	•	j scans every element, acting as the “reader”.
	•	i marks the position where the next non-zero element should be written.

At the start, both pointers sit at index 0.

As j moves forward, whenever it encounters a non-zero value, this value is placed at position i. Then i advances by one, preparing for the next non-zero element. If j sees a zero, nothing is written; the zero is simply skipped, because zeroes must end up at the back.

By the time j has scanned the entire array, all non-zero elements have been compacted at the front, in the correct order, occupying positions [0 … i−1]. The remaining portion of the array—from index i to the end—is then filled with zeroes. This step ensures that any leftover entries after the last non-zero are explicitly set to zero, completing the transformation.

This technique keeps the order of non-zero elements intact, because each non-zero value is written to the next available slot in the sequence in the same order as they originally appeared. Since each pointer only moves forward, and each element is processed at most once, the method is efficient and clean.

- **Time complexity:** O(n) - The algorithm scans through the array once with pointer `j`, and each non-zero is written exactly once by pointer `i`. No element is revisited or moved more than necessary, so the total amount of work grows linearly with the length of the array.
- **Space complexity:** O(1) - Only two integer pointers are used, and all modifications happen directly inside the original array. No extra arrays or data structures are created, so the additional memory used remains constant regardless of input size.