class Solution:
    def subarraysDivByK(self, a: List[int], k: int) -> int:
        n,r=len(a),[0]*k
        for i in range(1,n): a[i]+=a[i-1]
        for i in range(n): r[a[i]%k]+=1
        return sum(i*(i-1)//2 for i in r)+r[0]
