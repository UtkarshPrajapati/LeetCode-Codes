class Solution:
    def allPossibleFBT(self, n: int):
        dp={**{i:[] for i in range(0,n,2)},**{1:[TreeNode(0)]}}
        return (bt:=cache(lambda n: dp[n] if n in dp else [TreeNode(0,l,r) for i in range(n) for l in bt(i) for r in bt(n-i-1)]))(n)