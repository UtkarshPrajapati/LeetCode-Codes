class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s=set()
        def f(n):
            if not n: return
            s.add(n.val)
            f(n.left)
            f(n.right)
        f(root)
        return sorted(list(s))[k-1]