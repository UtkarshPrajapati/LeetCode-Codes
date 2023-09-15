class Solution:
    def myAtoi(self,s):
        match=re.match(r'^\s*([+-]?\d+)',s)
        return 0 if not match else max(-2**31,min(int(match.group(1)),2**31-1))