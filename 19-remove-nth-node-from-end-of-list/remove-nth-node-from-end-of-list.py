class Solution:
    def removeNthFromEnd(self, head, n):
        fast=slow=head
        for _ in range(n): fast=fast.next
        if not fast: return head.next
        while fast.next: fast,slow=fast.next,slow.next
        slow.next=slow.next.next
        return head