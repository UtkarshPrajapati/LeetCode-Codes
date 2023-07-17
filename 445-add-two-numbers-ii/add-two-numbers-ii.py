class Solution:
    def addTwoNumbers(self,l1,l2):
        s1,s2,d,c=[],[],ListNode(0),0
        while l1:s1.append(l1.val);l1=l1.next
        while l2:s2.append(l2.val);l2=l2.next
        while s1 or s2:
            t=c+(s1.pop() if s1 else 0)+(s2.pop() if s2 else 0)
            c=t//10
            (n:=ListNode(t%10)).next=d.next
            d.next=n
        if c>0: 
            (n:=ListNode(c)).next=d.next
            d.next=n
        return d.next