class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None: return ''
        s = str(root.val)
        if not root.left and not root.right: s += ''
        if root.left: s+='('+self.tree2str(root.left)+')'
        if not root.left and root.right: s += '()'
        if root.right: s += '('+self.tree2str(root.right)+')'
        return s        