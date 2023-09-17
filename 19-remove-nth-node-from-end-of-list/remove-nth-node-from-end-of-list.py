class Solution:
    def removeNthFromEnd(self,head,n):
        if not head.next: return 
        l,a=1,head
        while a.next:
            l,a=l+1,a.next
        if l==n: return head.next
        c,a=1,head
        while c!=l-n:
            c,a=c+1,a.next
        a.next=a.next.next
        return head