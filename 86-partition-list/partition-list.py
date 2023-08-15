class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1=ListNode(None)
        l2=ListNode(None)
        l1_head=l1
        l2_head=l2
        while head:
            if head.val<x: l1.next=ListNode(head.val);l1=l1.next
            else: l2.next=ListNode(head.val);l2=l2.next
            head=head.next
        l1.next=l2_head.next
        return l1_head.next