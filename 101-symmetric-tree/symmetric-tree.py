class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(l,r):
            if not l and not r: return True
            if not l or not r: return False
            if l.val!=r.val: return False
            return f(l.left,r.right) and f(l.right,r.left)
        return f(root.left, root.right)