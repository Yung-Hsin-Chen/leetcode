# Problem

You are given an integer array `cards` where `cards[i]` represents the value of the `ith` card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return `-1`.

 

Example 1:

> **Input:** cards = [3,4,2,3,4,7]\
> **Output:** 4\
> **Explanation:** We can pick up the cards `[3,4,2,3]` which contain a matching pair of cards with value `3`. Note that picking up the cards `[4,2,3,4]` is also optimal.

Example 2:

> **Input:** cards = [1,0,5,3]\
> **Output:** -1\
> **Explanation:** There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 

Constraints:

- `1 <= cards.length <= 105`
- `0 <= cards[i] <= 106`

# Solution

The goal is to find the minimum length of a consecutive subarray that contains at least one pair of matching cards. In other words, we want the shortest window that includes two cards with the same value.

A brute-force approach would check every possible subarray and see whether it contains duplicates, but that would take `O(n²)` time and is too slow for large inputs. Instead, this solution uses a hash map to track the most recent position of each card value.

We iterate through the array while maintaining a dictionary index that stores the last index where each card value appeared. For each card at position `i`, we check whether we have seen the same value before.
- If the value has been seen, then we can form a consecutive subarray from the previous index of that value to the current index. The length of that subarray is `i - index[c] + 1`. We update the answer with the minimum of the current answer and this length.
- Regardless of whether we found a match, we update `index[c] = i` so that we always keep the most recent occurrence of each value. This ensures that future matches produce the smallest possible window.

After scanning the entire array:
- If we found at least one matching pair, ans will contain the minimum window length.
- If no pair was found, we return `-1`.

### Complexity:

- **Time Complexity:** O(n) because we traverse the array once and each dictionary operation is constant time on average.
- **Space Complexity:** O(n) because we store the last index of each distinct card value.