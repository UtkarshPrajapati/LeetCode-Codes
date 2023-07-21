class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums);l=[1]*n;c=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        c[i] = c[j]
                    elif l[j] + 1 == l[i]: c[i] += c[j]
        return sum(c[i] for i in range(n) if l[i]==max(l))