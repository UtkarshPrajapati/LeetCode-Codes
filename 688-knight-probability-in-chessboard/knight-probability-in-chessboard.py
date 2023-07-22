class Solution:
    def knightProbability(self, n: int, k: int, r0: int, c0: int) -> float:
        l=defaultdict(list)
        for r,c in product(ra:=range(n),ra):
            for dx,dy in ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)):
                if 0<=(pos:=(r+dx,c+dy))[0]<n and 0<=pos[1]<n: l[(r,c)].append(pos)
        f=cache(lambda pos,h: 1 if h==k else sum(f(next_pos,h+1) for next_pos in l[pos]))
        return f((r0,c0),0)/8**k