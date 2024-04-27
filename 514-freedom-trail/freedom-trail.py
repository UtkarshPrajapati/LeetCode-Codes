class Solution:
    def findRotateSteps(self,ring,key):
        memo,positions={},defaultdict(list)
        for i,c in enumerate(ring): positions[c].append(i)
        def dp(ki,ri,pos,key,memo):
            if ki==len(key): return 0
            if (ki,ri) in memo: return memo[(ki,ri)]
            steps=float('inf')
            for i in pos[key[ki]]:
                steps=min(steps,min((i-ri)%len(ring),(ri-i)%len(ring))+dp(ki+1,i,pos,key,memo))
            memo[(ki,ri)]=steps+1
            return steps+1
        return dp(0,0,positions,key,memo)