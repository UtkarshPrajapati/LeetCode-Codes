class Solution:
    def rotateRight(self,head,k):
        if not head or not head.next: return head
        n,node=0,head
        while node:
            node=node.next
            n+=1
        k%=n
        new_tail=head
        for _ in range(n-k-1): new_tail=new_tail.next
        new_head=new_tail.next
        if not new_head: return head
        old_tail=new_head
        while old_tail.next: old_tail=old_tail.next
        old_tail.next=head
        new_tail.next=None
        return new_head