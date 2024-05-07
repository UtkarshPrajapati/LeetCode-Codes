# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10**6)
        num=0
        while head:
            num=num*10+head.val
            head=head.next
        num=str(num*2)
        h=n=ListNode(num[0])
        for d in num[1:]:
            n.next=ListNode(d)
            n=n.next
        return h