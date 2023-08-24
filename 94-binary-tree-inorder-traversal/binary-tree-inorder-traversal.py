class Solution:
    def inorderTraversal(self,root):
        s=[]
        def f(n):
            if not n: return
            f(n.left)
            s.append(n.val)
            f(n.right)
        f(root)
        return s