# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return
        slow=fast=head
        c=1
        prev=head
        while fast and fast.next:
            if c==1: c=0
            else: prev=prev.next
            slow,fast=slow.next,fast.next.next
        prev.next=prev.next.next
        return head