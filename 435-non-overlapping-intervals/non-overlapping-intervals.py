class Solution:
    def eraseOverlapIntervals(self, intv: List[List[int]]) -> int:
        end = float('-inf')
        return sum(1 if i[0] < end else (end := i[1], 0)[1] for i in sorted(intv, key=lambda x: x[1]))