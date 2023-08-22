class Solution:
    def addDigits(self, num: int) -> int:
        return [0,(1+(num-1)%9)][num!=0]