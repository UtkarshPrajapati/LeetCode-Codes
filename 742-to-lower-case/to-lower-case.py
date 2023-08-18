class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(ord(i)+32) if 65<=ord(i)<=90 else i for i in s)