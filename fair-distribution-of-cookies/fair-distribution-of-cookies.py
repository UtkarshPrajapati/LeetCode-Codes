class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unf=float('inf')
        d=[0]*k
        def backtrack(i):
            nonlocal min_unf,d
            if i == len(cookies): min_unf = min(min_unf, max(d));return
            if min_unf <= max(d): return
            for j in range(k):
                d[j] += cookies[i]
                backtrack(i + 1)
                d[j] -= cookies[i]
        backtrack(0)
        return min_unf