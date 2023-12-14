class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[float('inf')]*n for _ in range(n)]
        for u,v,w in times: adj[u-1][v-1]=w
        d=[float('inf')]*n
        d[k-1]=0
        tovis=[(0,k-1)]
        while tovis:
            dis,node=heappop(tovis)
            for i in range(n):
                if adj[node][i]!=float('inf') and dis+adj[node][i]<d[i]:
                    d[i]=dis+adj[node][i]
                    tovis.append((d[i],i))
        return max(d) if all(i!=float('inf') for i in d) else -1