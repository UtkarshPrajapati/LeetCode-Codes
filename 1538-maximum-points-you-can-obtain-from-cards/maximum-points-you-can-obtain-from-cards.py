class Solution:
    def maxScore(self, l: List[int], k: int) -> int:
        n=len(l)
        m=s=sum(l[:k])
        for i in range(1,k+1):
            s+=l[-i]-l[k-i]
            m=max(m,s)
        return m