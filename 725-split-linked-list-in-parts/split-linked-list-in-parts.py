class Solution:
    def splitListToParts(self,head,k):
        n,node=0,head
        while node:
            n+=1
            node=node.next
        (l,r),li=divmod(n,k),[]
        node=head
        for i in range(k):
            n1=a=ListNode(0)
            for _ in range(l):
                n1.next=ListNode(node.val)
                n1=n1.next
                if node.next: node=node.next
            if r>0:
                n1.next=ListNode(node.val)
                n1=n1.next
                if node.next: node=node.next
                r-=1
            li.append(a.next)
        return li