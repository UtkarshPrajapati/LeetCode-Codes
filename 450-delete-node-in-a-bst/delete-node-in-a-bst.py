class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def nmax(node):
            while node and node.right:
                node=node.right
            return node
        def nmin(node):
            while node and node.left:
                node=node.left
            return node
        r=root
        par=None
        while r:
            if r.val==key: break
            elif r.val>key: par=r;r=r.left
            else: par=r;r=r.right
        if not r: return root
        if r.left and r.right:
            n=nmax(r.left)
            r.val=n.val
            r.left=self.deleteNode(r.left,n.val)
        elif not par: root = r.left if r.left else r.right
        elif par.left == r: par.left = r.left if r.left else r.right
        elif par.right == r: par.right = r.left if r.left else r.right
        return root