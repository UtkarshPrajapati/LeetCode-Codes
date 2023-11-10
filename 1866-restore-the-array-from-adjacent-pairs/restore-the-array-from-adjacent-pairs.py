class Solution:
    def restoreArray(self, p):
        n,d=len(p),defaultdict(list)
        for a, b in p:
            d[a].append(b)
            d[b].append(a)
        st = next(e for e, cnt in Counter(chain(*p)).items() if cnt == 1)
        res,seen,n1=[st],{st},1
        while n1 < n + 1:
            st = next(ne for ne in d[st] if ne not in seen)
            res.append(st)
            seen.add(st)
            n1+=1
        return res