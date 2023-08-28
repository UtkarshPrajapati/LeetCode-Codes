# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s=[]
        for i in lists:
            a=i
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