class Solution:
    def oddEvenList(self,head):
        if not head: return
        odd=head
        evenHead=even=head.next
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenHead
        return head