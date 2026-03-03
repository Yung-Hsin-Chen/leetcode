from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = defaultdict(int)
        m_count = defaultdict(int)

        for r in ransomNote:
            r_count[r] += 1

        for m in magazine:
            m_count[m] += 1

        for r in r_count:
            if m_count[r] < r_count[r]:
                return False

        return True
    