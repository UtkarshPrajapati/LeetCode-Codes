class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in nums1:
            ind=nums2.index(i)
            for j in range(ind+1,len(nums2)):
                if nums2[j]>i: a.append(nums2[j]);break
            else: a.append(-1)
        return a