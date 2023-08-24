class Solution:
    def kthSmallest(self,root,k):
        res,k=[None],[k]
        def inorder(node):
            if not node: return
            inorder(node.left)
            k[0]-=1
            if k[0]==0: res[0]=node.val;return
            inorder(node.right)
        inorder(root)
        return res[0]