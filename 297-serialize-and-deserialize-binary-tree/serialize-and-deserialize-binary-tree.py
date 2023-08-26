class Codec:
    def serialize(self, root):
        s=[]
        def f(n):
            if not n: s.append(None);return
            s.append(n.val)
            f(n.left)
            f(n.right)
        f(root)
        return str(s)
    def deserialize(self, data):
        data = deque(eval(data))
        def f():
            if not data: return None
            val = data.popleft()
            if val is None: return None
            n = TreeNode(val)
            n.left = f()
            n.right = f()
            return n
        return f()