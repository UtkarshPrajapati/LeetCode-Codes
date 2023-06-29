class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n, arr, numOfKeys = len(grid), len(grid[0]), [], 0
        keys,locks = {c: i for i, c in enumerate('abcdef')},{c: i for i, c in enumerate('ABCDEF')}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@': heappush(arr, (0, i, j, 0))
                elif grid[i][j] in keys: numOfKeys += 1
        visited = set()
        while arr:
            steps, i, j, found = heappop(arr)
            curr = grid[i][j]
            if curr in locks and not (found >> locks[curr]) & 1 or curr == '#': continue
            if curr in keys:
                found |= 1 << keys[curr]
                if found == (1 << numOfKeys) - 1: return steps
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y, found) not in visited:
                    visited.add((x, y, found))
                    heappush(arr, (steps + 1, x, y, found))
        return -1