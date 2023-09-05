class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        d={None:None}
        n=head
        while n:
            d[n]=Node(n.val)
            n=n.next
        n=head
        while n:
            d[n].next=d[n.next]
            d[n].random=d[n.random]
            n=n.next
        return d[head]