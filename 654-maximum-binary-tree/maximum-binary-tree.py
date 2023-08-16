class Solution:
    def constructMaximumBinaryTree(self,nums):
        n,m=len(nums),max(nums)
        if nums is None: return None
        i,node=nums.index(m),TreeNode(m)
        if i: node.left=self.constructMaximumBinaryTree(nums[:i])
        if n-i-1: node.right=self.constructMaximumBinaryTree(nums[i+1:])
        return node