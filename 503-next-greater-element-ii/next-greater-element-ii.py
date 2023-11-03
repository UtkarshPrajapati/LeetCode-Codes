class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        a = []
        nums2 = nums + nums
        for ind in range(len(nums)):
            i = nums[ind]
            for j in range(ind + 1, len(nums2)):
                if nums2[j] > i: a.append(nums2[j]);break
            else: a.append(-1)
        return a