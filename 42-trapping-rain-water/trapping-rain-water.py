class Solution:
    def trap(self, a: List[int]) -> int:
        n=len(a)
        l,r=[a[0]]+[1]*(n-1),[1]*(n-1)+[a[-1]]
        for i in range(1,n):
            l[i],r[-i-1]=max(l[i-1], a[i]),max(r[-i],a[-i-1])
        return sum(min(l,r)-a for l,r,a in zip(l,r,a))