class Solution:
    def reverseBetween(self,head,left,right):
        prev,curr=None,head
        i=0
        while i<left-1:
            prev,curr=curr,curr.next
            i+=1
        ln,rn=prev,curr
        i=0
        while i<right-left+1:
            curr.next,prev,curr=prev,curr,curr.next
            i+=1
        if ln: ln.next=prev
        else: head=prev
        rn.next=curr
        return head