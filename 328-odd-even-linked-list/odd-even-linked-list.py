class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        a = head
        el = head.next
        el_head = el
        while el and el.next:
            a.next = el.next
            a = a.next
            el.next = a.next
            el = el.next
        a.next = el_head
        return head