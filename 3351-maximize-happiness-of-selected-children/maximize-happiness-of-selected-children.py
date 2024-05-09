class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse=True)
        return sum(max(h[i]-i,0) for i in range(k))