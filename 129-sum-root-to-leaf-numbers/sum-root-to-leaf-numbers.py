class Solution:
    def sumNumbers(self, root):
        def dfs(curr,num):
            if curr is None: return 0
            num=num*10+curr.val
            if not curr.left  and not curr.right: return num
            return dfs(curr.left,num)+dfs(curr.right,num)
        return dfs(root,0)