class Solution:
    def allPossibleFBT(self, n: int):
        return (f:=cache(lambda n,dp=(lambda:{**{i:[] for i in range(0,n,2)},**{1:[TreeNode(0)]}})(): dp[n] if n in dp else [TreeNode(0,l,r) for i in range(n) for l in f(i) for r in f(n-i-1)]))(n)