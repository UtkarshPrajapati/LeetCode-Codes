class Solution:
    def makeGood(self,s):
        s,i=list(s),0
        while i<len(s)-1:
            if abs(ord(s[i])-ord(s[i+1]))==32: 
                del s[i:i+2]
                if i>0: i-=1
            else: i+=1
        return ''.join(s)