# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10**6)
        l=''
        while head:
            l+=str(head.val)
            head=head.next
        l=list(str(int(l)*2))
        h=n=ListNode(l.pop(0))
        while l:
            n.next=ListNode(l.pop(0))
            n=n.next
        return h