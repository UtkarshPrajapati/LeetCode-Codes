class Solution:
    def makeConnected(self, n: int, c: List[List[int]]) -> int:
        if n-1>len(c): return -1
        def dfs(node,graph,v):
            v.add(node)
            for nei in graph[node]:
                if nei not in v: dfs(nei,graph,v)
        graph={i:[] for i in range(n)}
        for n1,n2 in c: graph[n1].append(n2);graph[n2].append(n1)
        v=set()
        comp=0
        for node in range(n):
            if node not in v: dfs(node,graph,v);comp+=1
        return comp-1