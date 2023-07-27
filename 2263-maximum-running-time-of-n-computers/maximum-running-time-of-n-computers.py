class Solution:
    def maxRunTime(self, n: int, bat: List[int]) -> int:
        i,j=1,sum(bat)//n 
        while i<j: 
            t=j-(j-i)//2 
            if sum(min(b,t) for b in bat)<t*n: j=t-1 
            else: i=t
        return i