class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=deque()
        for digit in num:
            while k>0 and stack and stack[-1]>digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        for _ in range(k):
            stack.pop()
        return ''.join(stack).lstrip('0') or "0"