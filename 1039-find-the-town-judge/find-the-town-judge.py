class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1: return 1
        d=defaultdict(list)
        r=list(range(1,n+1))
        t=set()
        for i,j in trust:
            d[j].append(i)
            t.add(i)
        print(d.items())
        for i,j in d.items():
            if set(r)-{i}==set(j) and i not in t: return i
        return -1