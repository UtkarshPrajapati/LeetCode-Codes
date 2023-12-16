class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        def dfs(node,g,v):
            v.add(node)
            for nei in g[node]:
                if nei not in v: dfs(nei,g,v)
        dx=defaultdict(list)
        dy=defaultdict(list)
        g=defaultdict(list)
        for i,s in enumerate(stones):
            dx[s[0]].append(i)
            dy[s[1]].append(i)
        for x in dx:
            for i,j in combinations(dx[x],2):
                g[i].append(j)
                g[j].append(i)
        for y in dy:
            for i,j in combinations(dy[y],2):
                g[i].append(j)
                g[j].append(i)
        v,comp=set(),0
        for node in range(n):
            if node not in v: dfs(node,g,v);comp+=1
        return n-comp