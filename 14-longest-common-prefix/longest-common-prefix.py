class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        for i in zip(*strs):
            res=set(i)
            if len(res)==1: ans+=res.pop()
            else: break
        return ans