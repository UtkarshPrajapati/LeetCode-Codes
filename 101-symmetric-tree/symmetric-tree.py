class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not root.left and not root.right: return True
        elif not root.left or not root.right: return False
        else:
            def f(l,r):
                if not l and not r: return True
                if not l or not r: return False
                if l.val!=r.val: return False
                return f(l.left,r.right) and f(l.right,r.left)
            return f(root.left, root.right)