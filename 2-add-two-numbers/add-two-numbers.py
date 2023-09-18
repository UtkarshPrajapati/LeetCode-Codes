class Solution:
    def addTwoNumbers(self,l1,l2):
        c=0;head=l3=ListNode(0)
        while l1 or l2 or c:
            val1,val2=l1.val if l1 else 0,l2.val if l2 else 0
            c,out=divmod(val1+val2+c,10)  
            l3.next=ListNode(out)
            l1,l2,l3=l1.next if l1 else None,l2.next if l2 else None,l3.next
        return head.next