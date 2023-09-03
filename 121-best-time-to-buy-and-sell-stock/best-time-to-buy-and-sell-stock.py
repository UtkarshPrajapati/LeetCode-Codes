class Solution:
    def maxProfit(self, A: List[int]) -> int:
        maxx,minn=0,A[0]
        for i in A:
            minn=min(minn,i)
            maxx=max(maxx,i-minn)
        return maxx