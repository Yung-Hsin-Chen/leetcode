class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        
        seen = set()
        for c in sentence:
            seen.add(c)

        return True if len(seen)==26 else False
    