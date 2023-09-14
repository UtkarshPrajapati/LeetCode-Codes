class Solution:
    def longestCommonPrefix(self,strs):
        s,l,r="",min(strs),max(strs)
        for i in range(min(len(l),len(r))):
            if l[i]!=r[i]: return s
            s+=l[i]
        return s 