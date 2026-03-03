from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for string in strs:
            ans["".join(sorted(string))].append(string)

        return list(ans.values())
    