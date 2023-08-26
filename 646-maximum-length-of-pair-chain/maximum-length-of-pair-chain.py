class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x : x[1])
        n=len(pairs)
        print(pairs)
        l=[pairs[0]]
        if n==1: return 1
        for i in range(n-1):
            if l[-1][1]<pairs[i+1][0]: l.append(pairs[i+1])
        return len(l)