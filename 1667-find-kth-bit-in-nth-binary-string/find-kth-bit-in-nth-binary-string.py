class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for _ in range(20):
            s += "1" + ''.join('0' if bit == '1' else '1' for bit in s)[::-1]
        return s[k-1]