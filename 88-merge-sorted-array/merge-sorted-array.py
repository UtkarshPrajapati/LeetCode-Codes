class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j=m-1,0
        nums1[:]=nums1[:m]
        while i>-1 and j<n:
            if nums1[i]>nums2[j]: nums1[i],nums2[j]=nums2[j],nums1[i];i-=1;j+=1
            else: break
        nums1.sort()
        nums2.sort()
        nums1[m+1:]=nums2