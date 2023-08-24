class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums);l=m=0;h=n-1
        while m<=h:
            if nums[m]==0: nums[l],nums[m]=nums[m],nums[l];l+=1;m+=1
            elif nums[m]==1: m+=1
            else: nums[m],nums[h]=nums[h],nums[m];h-=1