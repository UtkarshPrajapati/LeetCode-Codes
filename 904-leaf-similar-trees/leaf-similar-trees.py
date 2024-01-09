# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        st1=[]
        st2=[]
        def f1(n):
            if n.left: f1(n.left)
            if not n.left and not n.right: st1.append(n.val);return
            if n.right: f1(n.right)
        def f2(n):
            if n.left: f2(n.left)
            if not n.left and not n.right: st2.append(n.val);return
            if n.right: f2(n.right)
        f1(root1)
        f2(root2)
        print(st1,st2)
        return st1==st2