class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        l=[]
        def f(n,lev):
            if n.left: 
                if lev==len(l): l.append([])
                l[lev].append(n.left.val);f(n.left,lev+1)
            if n.right: 
                if lev==len(l): l.append([])
                l[lev].append(n.right.val);f(n.right,lev+1)
        l.append([root.val])
        f(root,1)
        return l