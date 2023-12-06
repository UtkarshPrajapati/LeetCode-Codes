class Solution:
    def postorderTraversal(self,root):
      s=[]
      def f(root):
        if not root: return
        f(root.left)
        f(root.right)
        s.append(root.val)
        return s
      return f(root)