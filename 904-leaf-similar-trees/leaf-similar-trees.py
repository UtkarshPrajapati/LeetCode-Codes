class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def f(n,st):
            if n.left: f(n.left,st)
            if not n.left and not n.right: st.append(n.val);return st
            if n.right: f(n.right,st)
            return st
        return f(root1,[])==f(root2,[])