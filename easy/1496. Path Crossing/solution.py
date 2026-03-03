class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }

        passed = {(0, 0)}
        curr_pos = (0, 0)

        for d in path:
            curr_pos = (curr_pos[0]+direction[d][0], curr_pos[1]+direction[d][1])
            if curr_pos in passed:
                return True
            passed.add(curr_pos)

        return False
    