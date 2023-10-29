class Solution:
    def poorPigs(self,buckets,minutesToDie,minutesToTest):
        if buckets==1: return 0
        a,b=int(minutesToTest/minutesToDie)+1,1
        while a**b<buckets: b+=1
        return b