class Solution:
    def restoreString(self, s: str, ind: List[int]) -> str:
        ss=list(s)
        for i in ind: ss[ind[i]]=s[i]
        return "".join(ss)