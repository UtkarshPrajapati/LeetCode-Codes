class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        return (lambda t: [t.insert(i,n) or t for i,n in zip(index,nums)] and t)([])