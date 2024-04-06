class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        c,i=0,0
        s=list(s)
        while i<len(s):
            if s[i]=='(': c+=1
            elif s[i]==')': c-=1
            if c<0: del s[i];c=0
            else: i+=1
        c,i=0,len(s)-1
        while i>=0:
            if s[i]==')': c+=1
            elif s[i]=='(': c-=1
            if c<0: del s[i];c=0
            i-=1        
        return ''.join(s)