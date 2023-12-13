class Solution:
    def findCheapestPrice(self,n,flights,src,dst,k):
        adj=[[] for _ in range(n)]
        for a,b,c in flights: adj[a].append((b,c))
        dist,q,s=[float('inf')]*n,deque([(src,0)]),0
        while q and s<=k:
            for _ in range(len(q)):
                node,pcost=q.popleft()
                for neigh,cost in adj[node]:
                    ncost=cost+pcost
                    if ncost>=dist[neigh]: continue
                    dist[neigh]=ncost
                    q.append((neigh,ncost))
            s+=1
        return -1 if dist[dst]==float('inf') else dist[dst]