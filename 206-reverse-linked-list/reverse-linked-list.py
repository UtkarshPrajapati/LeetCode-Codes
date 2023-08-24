class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nll=ListNode(None)
        t=nll
        st=[]
        n=head
        while n:
            st.append(n.val)
            n=n.next
        # print(st)
        # return head
        while len(st):
            
            nll.next=ListNode(st.pop())
            nll=nll.next
        return t.next