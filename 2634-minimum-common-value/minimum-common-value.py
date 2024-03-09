class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums1) & set(nums2)
        return min(a) if a else -1