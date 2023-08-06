class Solution:
    def maximum69Number(self, num: int) -> int:
        s=str(num)
        if "6" in s:
            i=s.index("6")
            return int(s[:i]+'9'+s[i+1:])
        return num