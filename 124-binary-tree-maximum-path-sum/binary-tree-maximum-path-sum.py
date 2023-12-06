class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.s=float('-inf')
        def f(node):
            if not node: return 0
            l,r=max(f(node.left),0),max(f(node.right),0)
            self.s=max(self.s,node.val+l+r)
            return node.val+max(l,r)
        f(root)
        return self.s