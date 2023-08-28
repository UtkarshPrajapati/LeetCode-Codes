class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s,a=[],head
        while a:
            s.append(a.val)
            a=a.next
        return s==s[::-1]