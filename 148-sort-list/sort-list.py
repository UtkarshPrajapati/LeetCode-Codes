class Solution:
    def sortList(self,head):
        if not head: return
        s,a=[],head
        while a:
            s.append(a.val)
            a=a.next
        s.sort(reverse=True)
        b=ll=ListNode()
        while s:
            ll.next=ListNode(s.pop())
            ll=ll.next
        return b.next