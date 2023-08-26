class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n=len(pairs)
        if n==1: return 1
        pairs.sort(key=lambda x:x[1])
        l,c=pairs[0][1],1
        for i in range(n-1):
            if l<pairs[i+1][0]: l=pairs[i+1][1];c+=1
        return c