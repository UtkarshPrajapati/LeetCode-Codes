class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n,ans=len(nums),[]
        nums.sort()
        for i in range(n):
            if i and nums[i]==nums[i-1]: continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]: continue
                k,l=j+1,n-1
                while k<l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if s==target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1;l-=1
                        while k<l and nums[k]==nums[k-1]: k+=1
                        while k<l and nums[l]==nums[l+1]: l-=1
                    elif s<target: k+=1
                    else: l-=1
        return ans