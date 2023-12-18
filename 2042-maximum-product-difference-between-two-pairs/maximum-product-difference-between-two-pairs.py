class Solution:
    def maxProductDifference(self,nums):
            mi1,mi2,ma1,ma2=float('inf'),float('inf'),float('-inf'),float('-inf')
            for i in nums:
                if i<=mi1: mi1,mi2=i,mi1
                elif i<mi2: mi2=i
                if i>=ma1: ma1,ma2=i,ma1
                elif i>ma2: ma2=i
            return ma1*ma2-mi1*mi2