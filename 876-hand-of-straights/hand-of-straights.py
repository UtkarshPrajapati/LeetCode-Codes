class Solution:
    def isNStraightHand(self,hand,s):
        n=len(hand)
        if n%s!=0: return False
        count=Counter(hand)
        while count:
            m=min(count)
            for k in range(m,m+s):
                v=count.get(k,0)
                if v==0: return False
                if v==1: count.pop(k)
                else: count[k]=v-1
        return True