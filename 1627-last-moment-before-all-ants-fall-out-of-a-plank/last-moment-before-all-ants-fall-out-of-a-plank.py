class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        if left: time = max(time, max(pos for pos in left))
        if right: time = max(time, max(n-pos for pos in right))
        return time