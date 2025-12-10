# Problem

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

Note that an integer is said to be common to `nums1` and `nums2` if both arrays have at least one occurrence of that integer.

 

Example 1:

> **Input:** nums1 = [1,2,3], nums2 = [2,4]\
> **Output:** 2\
> **Explanation:** The smallest element common to both arrays is 2, so we return 2.

Example 2:

> **Input:** nums1 = [1,2,3,6], nums2 = [2,3,4,5]\
> **Output:** 2\
> **Explanation:** There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 

Constraints:

- `1 <= nums1.length, nums2.length <= 105`
- `1 <= nums1[i], nums2[j] <= 109`
- Both `nums1` and `nums2` are sorted in non-decreasing order.

# Solution

Both arrays are already sorted in non-decreasing order. This ordering gives us a natural way to compare them without ever needing extra data structures or nested loops.

Place one pointer at the start of each array. These pointers represent the current candidate numbers we are comparing. At each step, look at nums1[i] and nums2[j].

If the number in the first array is smaller than the number in the second, then the smaller number can never match a later number in the other array, because the other array is sorted and can only move upward. To give it a chance to find a match, we advance the pointer in the first array.

Likewise, if the number in the second array is smaller, we advance its pointer. This gently pushes both pointers forward through their arrays, skipping numbers that cannot possibly participate in the smallest common value.

The moment the two numbers match, we have found the smallest integer that appears in both arrays. It must be the smallest such value because both pointers only ever move forward, and we check numbers in increasing order. At that point we simply return the value.

If one pointer reaches the end of its array before any match is found, then there is no number common to both arrays, and the answer is –1.

This approach works efficiently because each pointer moves forward at most once per comparison. No element is revisited or rescanned, and no additional storage is needed.

- **Time complexity:** O(n+m)
- **Space complexity:** O(1)