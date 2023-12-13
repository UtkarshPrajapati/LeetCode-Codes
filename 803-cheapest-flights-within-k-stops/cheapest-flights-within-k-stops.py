class Solution:
    def findCheapestPrice(self,n,flights,src,dst,k):
        f=[[] for __ in range(n)]
        for a,b,p in flights: f[a].append((b,p))
        heap,d=[(0,src,k+1)],[[math.inf]*(k+2) for _ in range(n)]
        while heap:
            p,u,k=heappop(heap)
            if u==dst: return p
            if k>0:
                for v,w in f[u]:
                    nd=p+w
                    if nd<d[v][k-1]:
                        d[v][k-1]=nd
                        heappush(heap,(nd,v,k-1))
        return -1