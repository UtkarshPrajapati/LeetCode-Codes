class Solution:
    sys.set_int_max_str_digits(10**6)
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for digit in num:
            while k>0 and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        while k>0 and stack:
            stack.pop()
            k-=1
        return str(int(''.join(stack))) if stack else "0"