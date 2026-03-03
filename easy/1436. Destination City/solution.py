class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        outgoing = set()
        ingoing = set()

        for path in paths:
            outgoing.add(path[0])
            ingoing.add(path[1])

        return list(ingoing-outgoing)[0]
    