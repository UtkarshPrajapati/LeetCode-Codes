class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==1: return nums
        e1,c1,e2,c2=float('-inf'),0,float('-inf'),0
        for i in range(n):
            if c1==0 and nums[i]!=e2: c1=1;e1=nums[i]
            elif c2==0 and nums[i]!=e1: c2=1;e2=nums[i]
            elif nums[i]==e1: c1+=1
            elif nums[i]==e2: c2+=1
            else: c1-=1;c2-=1
        c1,c2,l=0,0,[]
        for i in range(n):
            if nums[i]==e1: c1+=1
            if nums[i]==e2: c2+=1
        m=n//3+1
        if c1>=m: l.append(e1)
        if c2>=m: l.append(e2)
        return l