class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        c=0
        def ino(n):
            nonlocal c
            if n:
                ino(n.left)
                if low<=n.val<=high: c+=n.val
                if n.val<high: ino(n.right)
        ino(root)
        return c