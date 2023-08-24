class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n,res=len(nums),[]
        for i in range(1<<n):
            sub=[]
            for j in range(n):
                if i&(1<<j): sub.append(nums[j])
            res.append(sub)
        return res