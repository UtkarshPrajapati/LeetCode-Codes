class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        l=[]
        def f(n,lev):
            if lev==len(l): l.append([])
            l[lev].insert(0,n.val) if lev%2 else l[lev].append(n.val)
            for c in [n.left,n.right]:
                if c: f(c,lev+1)
        f(root,0)
        return l