class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        s=defaultdict(list)
        def f1(n,l):
           if n:
               s[l].append(n.val)
               f1(n.left,l+1)
               f1(n.right,l+1)
        def f2(l,d):
            if not l: return True
            if d%2==0:
                if l[0] % 2 == 0: return False
                return all(l[i]%2==1 and l[i]>l[i-1] for i in range(1,len(l)))
            else:
                if l[0] % 2 == 1: return False
                return all(l[i]%2==0 and l[i]<l[i-1] for i in range(1,len(l)))
        f1(root,0)
        return all(f2(v,k%2) for k,v in s.items())