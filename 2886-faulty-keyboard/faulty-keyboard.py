class Solution:
    def finalString(self, s: str) -> str:
        a=""
        for i in s:
            a=a[::-1] if i=="i" else a+i
        return a