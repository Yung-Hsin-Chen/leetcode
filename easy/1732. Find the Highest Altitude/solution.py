class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = 0
        curr = 0
        for g in gain:
            curr += g
            max_altitude = max(max_altitude, curr)
        return max_altitude
    