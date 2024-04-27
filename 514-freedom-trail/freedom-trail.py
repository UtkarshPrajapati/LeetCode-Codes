class Solution:
    def findRotateSteps(self,ring,key):
        memo,positions={},defaultdict(list)
        for i,c in enumerate(ring): positions[c].append(i)
        return self.dp(0,0,positions,key,ring,memo)
    def dp(self,ki,ri,pos,key,ring,memo):
        if ki==len(key): return 0
        if (ki,ri) in memo: return memo[(ki,ri)]
        steps=float('inf')
        for i in pos[key[ki]]:
            steps=min(steps,min((i-ri)%len(ring),(ri-i)%len(ring))+self.dp(ki+1,i,pos,key,ring,memo))
        memo[(ki,ri)]=steps+1
        return steps+1