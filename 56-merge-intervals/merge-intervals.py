class Solution:
    def merge(self, intv: List[List[int]]) -> List[List[int]]:
        intv.sort(key=lambda x: x[0])
        l=[]
        for i in intv:
            if not l or l[-1][1]<i[0]: l.append(i)
            else: l[-1][1]=max(l[-1][1],i[1])
        return l