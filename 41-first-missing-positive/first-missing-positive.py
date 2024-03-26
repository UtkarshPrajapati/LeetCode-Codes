class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(filter(lambda x:x>0,nums))
        c=1
        while True:
            if c not in s: return c
            c+=1