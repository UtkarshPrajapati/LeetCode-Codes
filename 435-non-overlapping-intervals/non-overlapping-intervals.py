class Solution:
    def eraseOverlapIntervals(self, intv: List[List[int]]) -> int:
        end,c = float('-inf'),0
        for i in sorted(intv, key=lambda x: x[1]):
            if i[0]<end: c+=1
            else: end=i[1]
        return c