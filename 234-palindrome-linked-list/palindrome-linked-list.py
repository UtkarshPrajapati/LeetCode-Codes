class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        prev=None
        while slow:
            slow.next,prev,slow=prev,slow,slow.next
        slow=head
        while slow and prev:
            if slow.val!=prev.val: return False
            slow,prev=slow.next,prev.next
        return True