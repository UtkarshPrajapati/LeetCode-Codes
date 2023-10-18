class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g,dp=[[] for _ in range(n)],[-1]*n 
        for prev,next in relations:
            g[prev-1].append(next-1)
        def f(course):
            if dp[course]!=-1: return dp[course]
            dp[course]=time[course] if not g[course] else max(f(prereq) for prereq in g[course])+time[course]
            return dp[course]
        return max(f(course) for course in range(n))