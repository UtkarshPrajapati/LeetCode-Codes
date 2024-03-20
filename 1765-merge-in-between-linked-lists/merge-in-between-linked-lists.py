# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        an=list1
        bn=list1
        for _ in range(a-1):
            an=an.next
        for _ in range(b+1):
            bn=bn.next
        end=list2
        while end.next:
            end=end.next
        an.next=list2
        end.next=bn
        return list1