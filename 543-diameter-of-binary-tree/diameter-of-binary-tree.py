class Solution:
    def diameterOfBinaryTree(self,root):
      d=0
      def f(node):
        nonlocal d
        if not node: return 0
        l,r=f(node.left),f(node.right)
        d=max(d,l+r)
        return max(l,r)+1
      f(root)
      return d