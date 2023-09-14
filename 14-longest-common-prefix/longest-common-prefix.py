class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s,l,r="",strs[0],strs[-1]
        for i in range(min(len(l),len(r))):
            if l[i]!=r[i]: return s
            s+=l[i]
        return s 