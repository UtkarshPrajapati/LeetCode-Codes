class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        if not root: return TreeNode(t)
        n=root
        while True:
            if n.val>t:
                if not n.left: n.left=TreeNode(t);break
                else: n=n.left
            else:
                if not n.right: n.right=TreeNode(t);break
                else: n=n.right
        return root