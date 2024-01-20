class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res,A,s=0,[-inf]+arr+[-inf],[]
        for i,x in enumerate(A):
            while s and A[s[-1]]>x:
                j=s.pop()
                res+=A[j]*(i-j)*(j-s[-1])
            s.append(i)
        return res%1000000007