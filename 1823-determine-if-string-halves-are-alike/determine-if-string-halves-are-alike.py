class Solution:
    def halvesAreAlike(self,s):
        n=len(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        return sum(1 for i in s[:n//2] if i in vowels)==sum(1 for i in s[n//2:] if i in vowels)