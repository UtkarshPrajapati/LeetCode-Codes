class Solution:
    def fullBloomFlowers(self,A,persons):
        s,e=sorted(a for a,_ in A),sorted(b for _,b in A)
        return [bisect_right(s,p)-bisect_left(e,p) for p in persons]