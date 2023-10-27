class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n,c,f=len(nums),0,True
        for i in range(n):
            if i!=n-1 and nums[i]==nums[i+1]:
                if f and i%2==0: c+=1;f=False
                elif not f and i%2==1: c+=1;f=True
        return c+1 if (n-c)%2 else c