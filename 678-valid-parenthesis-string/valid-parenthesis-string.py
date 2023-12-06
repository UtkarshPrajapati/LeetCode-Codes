class Solution:
    def checkValidString(self,s):
        i=j=0
        for c in s:
            i+=1 if c=='(' else -1
            j+=1 if c!=')' else -1
            if j<0: break
            i=i if i>0 else 0
        return i==0