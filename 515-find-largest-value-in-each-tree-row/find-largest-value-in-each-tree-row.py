class Solution:
    def largestValues(self,root):
        d = defaultdict(list)
        def f(l,n):
            if n:
                if n.left:
                    d[l].append(n.left.val)
                    f(l+1,n.left)
                if n.right:
                    d[l].append(n.right.val)
                    f(l+1,n.right)
        if root: d[0].append(root.val)
        f(1,root)
        return [max(i) for i in d.values()]