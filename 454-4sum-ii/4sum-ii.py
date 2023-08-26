class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt,dic=0,defaultdict(int)
        for a in A:
            for b in B: dic[a+b]+=1
        for c in C:
            for d in D: cnt+=dic[-(c+d)]
        return cnt