class Solution:
    def restoreString(self, s: str, ind: List[int]) -> str:
        r=""
        for i in range(len(ind)): r+=s[ind.index(i)]
        return r