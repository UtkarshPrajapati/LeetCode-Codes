class Solution:
    def rearrangeArray(self,A):
        n=len(A);ans,pi,ni=[0]*n,0,1
        for i,ch in enumerate(A):
            if ch<0: ans[ni]=ch;ni+=2
            else: ans[pi]=ch;pi+=2
        return ans