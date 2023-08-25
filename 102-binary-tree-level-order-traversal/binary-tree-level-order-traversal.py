class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        l=defaultdict(list)
        def f(n,lev):
            if not n: return
            if n.left: l[lev].append(n.left.val);f(n.left,lev+1)
            if n.right: l[lev].append(n.right.val);f(n.right,lev+1)
        l[0].append(root.val)
        f(root,1)
        return list(l.values())