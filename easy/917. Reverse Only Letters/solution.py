class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s_list[l].isalpha():
                l += 1
            while l < r and not s_list[r].isalpha():
                r -= 1
            tmp = s_list[l]
            s_list[l] = s_list[r]
            s_list[r] = tmp
            l += 1
            r -= 1
        return "".join(s_list)