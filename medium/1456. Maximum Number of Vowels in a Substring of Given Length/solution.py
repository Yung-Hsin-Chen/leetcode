class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        num_vowel = 0
        for i in range(k):
            if s[i] in vowels:
                num_vowel += 1
        l = 0
        max_vowel = num_vowel
        for r in range(k, len(s)):
            if s[r] in vowels:
                num_vowel += 1
            if s[l] in vowels:
                num_vowel -= 1
            l += 1
            max_vowel = max(max_vowel, num_vowel)
        return max_vowel
    