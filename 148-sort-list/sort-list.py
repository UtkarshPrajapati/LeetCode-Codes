# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        s=[]
        a=head
        while a:
            s.append(a.val)
            a=a.next
        s.sort()
        print(s)
        ll=ListNode()
        b=ll
        while s:
            ll.next=ListNode(s.pop(0))
            ll=ll.next
        return b.next