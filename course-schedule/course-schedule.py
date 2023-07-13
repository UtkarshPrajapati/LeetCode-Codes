class Solution:
    def canFinish(self, n, p):
        d = defaultdict(list)
        for pre, c in p: d[c].append(pre)
        visited = set()
        def dfs(c):
            if c in visited: return False
            visited.add(c)
            if not all(dfs(pre) for pre in d[c]): return False
            visited.remove(c)
            d[c] = []
            return True
        return all(dfs(i) for i in range(n))