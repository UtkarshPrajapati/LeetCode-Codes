class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i,j=list1,list2
        nl=ListNode(None)
        a=nl
        while i or j:
            if i and j: 
                if i.val<j.val: nl.next=ListNode(i.val);i=i.next
                else: nl.next=ListNode(j.val);j=j.next
            else:
                if i: nl.next=ListNode(i.val);i=i.next
                if j: nl.next=ListNode(j.val);j=j.next
            nl=nl.next
        return a.next