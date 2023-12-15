class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], thres: int) -> int:
        adj=defaultdict(list)
        for f,t,w in edges: adj[f].append((t,w));adj[t].append((f,w))
        min_city=-1
        min_nei=float('inf')
        for i in range(n):
            d=[float('inf')]*n
            d[i]=0
            q=[(0,i)]
            while q:
                dist,node=heapq.heappop(q)
                if dist!=d[node]: continue
                for nei,w in adj[node]:
                    if d[node]+w<d[nei] and d[node]+w<=thres:
                        d[nei]=d[node]+w
                        heapq.heappush(q,(d[nei],nei))
            cnt=sum(dist<=thres for dist in d)
            if cnt<=min_nei: min_city,min_nei=i,cnt
        return min_city