class Solution:
    def detectCycle(self,head):
        dp={}
        while head:
            if head in dp: return head
            dp[head]=None
            head=head.next