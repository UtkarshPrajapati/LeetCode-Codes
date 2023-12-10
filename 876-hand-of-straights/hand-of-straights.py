class Solution:
    def isNStraightHand(self, hand: List[int], s: int) -> bool:
        n=len(hand)
        if n%s!=0: return False
        count=Counter(hand)
        while count:
            m=min(count)
            for k in range(m,m+s):
                v=count[k]
                if not v: return False
                if v==1: del count[k]
                else: count[k]=v-1
        return True