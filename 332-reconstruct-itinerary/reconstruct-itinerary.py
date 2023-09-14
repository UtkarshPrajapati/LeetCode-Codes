class Solution:
    def findItinerary(self,tickets):
        d=defaultdict(list)
        for i in tickets:
            d[i[0]].append(i[1])
        for dest in d.values():
            dest.sort(reverse=True)
        st,res=["JFK"],[]
        while st:
            cur=st[-1]
            if d[cur]: st.append(d[cur].pop())
            else: res.append(st.pop())
        res.reverse()
        return res