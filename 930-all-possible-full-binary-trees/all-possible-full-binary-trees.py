class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        dp = [[], [TreeNode(0)]] + [[] for _ in range(n - 1)]
        for i in range(3, n + 1, 2):
            dp[i] = [TreeNode(0, l, r) for j in range(1, i, 2) for l in dp[j] for r in dp[i - j - 1]]
        return dp[n]