class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        c=0
        r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        d={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        i=0
        while i<n:
            if s[i:i+2] in d: c+=d[s[i:i+2]];i+=2
            else: c+=r[s[i]];i+=1
        return c