class Solution:
    def evenOddBit(self,n):
        return [(int('0101010101',2)&n).bit_count(),(int('1010101010',2)&n).bit_count()]