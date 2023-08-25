class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r,n,res=[1],[1],len(nums),[]
        for i in range(1,n): l.append(l[-1]*nums[i-1])
        for i in range(n-2,-1,-1): r.append(r[-1]*nums[i+1])
        for i in range(n): res.append(l[i]*r[n-i-1])
        return res