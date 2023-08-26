class Solution:
    def getIntersectionNode(self,headA,headB):
        if headA and headB:
            a,b=headA,headB
            while a!=b:
                a=a.next if a else headB
                b=b.next if b else headA
            return b