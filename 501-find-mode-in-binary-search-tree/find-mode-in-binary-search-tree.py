# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def h(node,l):
            if node is None:
                return l
            if(node.val in l):
                l[node.val]+=1
            else:
                l[node.val]=1
            if(node.left is not None):
                h(node.left,l)
            if(node.right is not None):
                h(node.right,l)
            return l
        l=dict()
        h(root,l)
        m=max(l.values())
        return (i for i,v in l.items() if(v==m))