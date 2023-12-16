class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        def dfs(node,g,v):
            v.add(node)
            for nei in g[node]:
                if nei not in v: dfs(nei,g,v)
        g=defaultdict(list)
        for i,x in enumerate(stones):
            for j,y in enumerate(stones):
                if x[0]==y[0] or x[1]==y[1]: g[i].append(j)
        v,comp=set(),0
        for node in range(n):
            if node not in v: dfs(node,g,v);comp+=1
        return n-comp