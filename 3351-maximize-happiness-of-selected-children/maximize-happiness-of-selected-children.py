class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse=True)
        s=0
        for i in range(k):
            a=h[i]-i
            if a>0: s+=a
        return s