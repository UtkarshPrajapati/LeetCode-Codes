class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        l=[]
        def f(n,lev):
            if lev==len(l): l.append([])
            l[lev].insert(0,n.val) if lev%2 else l[lev].append(n.val)
            if n.left: f(n.left,lev+1)
            if n.right: f(n.right,lev+1)
        f(root,0)
        return l