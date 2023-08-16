class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s,l,r="",strs[0],strs[-1]
        for i in range(min(len(l),len(r))):
            a=l[i]
            if a!=r[i]: return s
            s+=a
        return s 