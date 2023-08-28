class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s=[]
        for i in lists:
            a=i
            while a:
                s.append(a.val)
                a=a.next
        s.sort()
        ll=ListNode()
        b=ll
        while s:
            ll.next=ListNode(s.pop(0))
            ll=ll.next
        return b.next