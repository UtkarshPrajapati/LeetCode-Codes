class Solution:
    def minDeletion(self,nums):
        n,c,f=len(nums),0,True
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                if f and i%2==0: c+=1;f=False
                elif not f and i%2==1: c+=1;f=True
        if n>1 and nums[-2]==nums[-1] and ((f and n%2==0) or (not f and n%2==1)): c+=1
        return c+1 if (n-c)%2 else c