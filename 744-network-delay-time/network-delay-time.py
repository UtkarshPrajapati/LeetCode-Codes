class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u-1].append((v-1, w))
        d = [float('inf')] * n
        d[k-1] = 0
        tovis = deque([(0, k-1)])
        while tovis:
            dis, node = tovis.popleft()
            for nei, w in adj[node]:
                if dis + w < d[nei]:
                    d[nei] = dis + w
                    tovis.append((d[nei], nei))
        return max(d) if all(i != float('inf') for i in d) else -1