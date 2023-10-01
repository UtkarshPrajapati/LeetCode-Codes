class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        s=s.split(" ")
        for i in s:
            ans+=i[::-1]+" "
        return ans[:-1]