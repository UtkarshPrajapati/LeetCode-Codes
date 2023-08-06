class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n1=len(nums1);x=n1//2
        if n1&1: return nums1[x]
        return (nums1[x-1]+nums1[x])/2