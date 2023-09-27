class Solution:
    def decodeAtIndex(self,s,k):
        l=i=0
        while l<k:
            l,i=l*int(s[i]) if s[i].isdigit() else l+1,i+1
        for j in range(i-1,-1,-1):
            char=s[j]
            if char.isdigit():
                l//=int(char)
                k%=l
            else:
                if k==0 or k==l: return char
                l-=1