class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2: return False
        cs,ps=0,{0:-1}
        for i,n in enumerate(nums):
            cs=(cs+n)%k
            if cs in ps:
                if i-ps[cs]>1: return True
            else: ps[cs]=i
        return False