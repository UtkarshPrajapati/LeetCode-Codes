class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def f(l,r):
            if l>r: return None
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            root.left=f(l,mid-1)
            root.right=f(mid+1,r)
            return root
        return f(0,len(nums)-1)