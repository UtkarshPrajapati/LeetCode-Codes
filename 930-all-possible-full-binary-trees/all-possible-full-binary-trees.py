class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []
        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, n + 1, 2):
            for j in range(1, i, 2):
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        dp[i].append(root)
        return dp[n]
