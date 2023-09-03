class Solution:
    def rearrangeArray(self,A):
        n=len(A);ans,pi,ni=[0]*n,0,1
        for i in range(n):
            if A[i]<0: ans[ni]=A[i];ni+=2
            else: ans[pi]=A[i];pi+=2
        return ans