class Solution:    
    def shortestPathLength(self,graph):
        n=len(graph)
        dist,q=[[[float('inf')]*n for _ in range(1<<n)] for _ in range(n)],deque([(i,1<<i,i) for i in range(n)])
        for i in range(n): dist[i][1<<i][i]=0
        while q:
            node,mask,head=q.popleft()
            d=dist[node][mask][head]
            if mask==(1<<n)-1: return d
            for v in graph[node]:
                mask_v=mask|(1<<v)
                if d+1<dist[v][mask_v][node]:
                    dist[v][mask_v][node]=d+1
                    q.append((v,mask_v,node))
        return float('inf')