class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        root.next=None
        def f(n,lev):
            if n.left: n.left.next=n.right
            if n.right and n.next: n.right.next=n.next.left
            if n.left: f(n.left,lev+1)
            if n.right: f(n.right,lev+1)
        f(root,0)
        return root