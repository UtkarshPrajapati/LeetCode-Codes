class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unf = float('inf')
        distribution = [0] * k
        def backtrack(i):
            nonlocal min_unf, distribution
            if i == len(cookies): min_unf = min(min_unf, max(distribution));return
            if min_unf <= max(distribution): return
            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]
        backtrack(0)
        return min_unf