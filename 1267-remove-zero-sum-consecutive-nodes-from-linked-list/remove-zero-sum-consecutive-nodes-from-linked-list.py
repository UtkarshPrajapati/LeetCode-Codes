class Solution:
	def removeZeroSumSublists(self,head):
		nn=ListNode(0,head)
		ps=0
		d={0:nn}
		while head:
			ps+=head.val
			d[ps]=head
			head=head.next
		head=nn
		ps=0
		while head:
			ps+=head.val
			head.next=d[ps].next
			head=head.next
		return nn.next