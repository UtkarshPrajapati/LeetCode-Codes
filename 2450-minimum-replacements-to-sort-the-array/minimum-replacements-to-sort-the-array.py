class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n,l,ans=len(nums),nums[-1],0
        for i in range(n-1,-1,-1):
            st=(nums[i]-1)//l
            l=nums[i]//(st+1)
            ans+=st
        return ans