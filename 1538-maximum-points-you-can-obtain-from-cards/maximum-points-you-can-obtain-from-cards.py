class Solution:
    def maxScore(self, l: List[int], k: int) -> int:
        n=len(l)
        m=s=sum(l[:k])
        for i in range(k):
            s-=l[k-i-1]-l[n-i-1]
            m=max(m,s)
        return m