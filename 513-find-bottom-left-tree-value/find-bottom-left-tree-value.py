# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        st=defaultdict(list)
        def f(n,l):
            if n:
                st[l].append(n.val)
                f(n.left,l+1)
                f(n.right,l+1)
        f(root,0)
        return st[max(st.keys())][0]