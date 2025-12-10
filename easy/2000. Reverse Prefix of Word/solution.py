class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        ch_exist = False
        i, j = 0, 0
        while (i<len(word)) and (j<len(word)) and (i<=j):
            if word[j]==ch:
                ch_exist = True
            if not ch_exist:
                j += 1
            else:
                tmp = word[i]
                word_list[i] = word_list[j]
                word_list[j] = tmp
                i += 1
                j -= 1
        return "".join(word_list)
                