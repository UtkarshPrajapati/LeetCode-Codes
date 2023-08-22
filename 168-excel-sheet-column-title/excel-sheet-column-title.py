class Solution:
    def convertToTitle(self,n):
        a=[]
        while n:
            n,r=divmod(n-1,26)
            a.append(chr(65+r))
        return ''.join(reversed(a))