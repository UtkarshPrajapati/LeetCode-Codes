class Solution:
    def countAsterisks(self, s: str) -> int:
        cbar,c=0,0
        for i in s:
            cbar+=i=="|"
            c+=i=="*" and cbar%2==0
        return c