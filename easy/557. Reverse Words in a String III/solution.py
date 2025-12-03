class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        words = s.split(" ")
        for word in words:
            word = list(word)
            l, r = 0, len(word)-1
            while l < r:
                tmp = word[l]
                word[l] = word[r]
                word[r] = tmp
                l += 1
                r -= 1
            ans.append("".join(word))
        return " ".join(ans)
