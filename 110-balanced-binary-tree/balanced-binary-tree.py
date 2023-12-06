class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node: return 0
            l, r = height(node.left), height(node.right)
            if l < 0 or r < 0 or abs(l - r) > 1: return -1
            return max(l, r) + 1
        return height(root) >= 0