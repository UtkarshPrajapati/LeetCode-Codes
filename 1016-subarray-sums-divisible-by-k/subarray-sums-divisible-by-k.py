class Solution:
    def subarraysDivByK(self, a: List[int], k: int) -> int:
        n=len(a);p,r=[0]*(n+1),[0]*k
        for i in range(n): p[i+1]=p[i]+a[i]
        for i in range(n+1): r[p[i]%k]+=1
        return sum(i*(i-1)//2 for i in r)