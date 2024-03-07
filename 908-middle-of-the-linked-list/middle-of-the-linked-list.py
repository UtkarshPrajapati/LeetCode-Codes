class Solution:
    def middleNode(self,head):
        if head is None or head.next is None: return head
        slow=fast=head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        return slow