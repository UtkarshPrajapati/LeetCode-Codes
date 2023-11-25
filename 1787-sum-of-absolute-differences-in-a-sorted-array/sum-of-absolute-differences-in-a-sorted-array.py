class Solution:
    def getSumAbsoluteDifferences(self,nums):
        n=len(nums)
        l = [0]
        for i in range(n):
            l.append(l[-1] + nums[i])
        return [nums[i]*(i+i-n)-2*l[i]+l[n] for i in range(n)]