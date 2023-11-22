class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                d[i+j].append(val)
        return [val for key in sorted(d.keys()) for val in reversed(d[key])]