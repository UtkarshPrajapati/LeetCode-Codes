class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def f(node,mi,ma):
            if not node: return ma-mi
            ma,mi=max(ma,node.val),min(mi,node.val)
            return max(f(node.left,mi,ma),f(node.right,mi,ma))
        return f(root,root.val,root.val)