class Solution:
    def restoreArray(self,p):
        n,d=len(p),defaultdict(list)
        for a,b in p:
            d[a].append(b)
            d[b].append(a)
        res=[[e for e,cnt in Counter(chain(*p)).items() if cnt==1][0]]
        seen=set(res)
        n1=1
        while n1<n+1:
            for ne in d[res[-1]]:
                if ne not in seen: res.append(ne);seen.add(ne);n1+=1
        return res