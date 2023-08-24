class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def f(node,d):
            if node.left and node.right: return max(f(node.left,d),f(node.right,d))+1
            elif node.left: return f(node.left,d)+1
            elif node.right: return f(node.right,d)+1
            else: return 1
        return f(root,0)