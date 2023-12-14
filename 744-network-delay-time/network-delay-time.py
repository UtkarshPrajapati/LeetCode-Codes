class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u-1].append((v-1, w))
        d = [float('inf')] * n
        d[k-1] = 0
        tovis = [(0, k-1)]
        while tovis:
            dis, node = heappop(tovis)
            for nei, w in adj[node]:
                if dis + w < d[nei]:
                    d[nei] = dis + w
                    heappush(tovis, (d[nei], nei))
        # return max(d) if all(i != float('inf') for i in d) else -1
        ans=-1
        for i in d:
            if i==float("inf"):
                return -1
            ans=max(ans,i)
        return ans
        
