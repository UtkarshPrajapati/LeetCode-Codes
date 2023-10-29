class Solution:
    def numberOfSteps(self, num: int) -> int:
        n=0
        while num:
            num=num-1 if num&1 else num>>1
            n+=1
        return n