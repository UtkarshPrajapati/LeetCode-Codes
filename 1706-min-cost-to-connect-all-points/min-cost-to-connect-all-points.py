class Solution:
    def minCostConnectPoints(self,p):
        def find(parent,x):
            if parent[x]==x: return x
            parent[x]=find(parent,parent[x])
            return parent[x]
        def union(parent,x,y):
            parent[find(parent,x)]=find(parent,y)
        n=len(p)
        edges=sorted([(abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1]),i,j) for i in range(n) for j in range(i+1,n)])
        parent=list(range(n))
        min_cost,num_edges=0,0
        for cost,u,v in edges:
            if find(parent,u)!=find(parent,v):
                union(parent,u,v)
                min_cost+=cost
                num_edges+=1
                if num_edges==n-1: break
        return min_cost