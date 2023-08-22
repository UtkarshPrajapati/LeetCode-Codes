class Solution:
    def countAsterisks(self, s: str) -> int:
        cbar,c=0,0
        for i in s:
            if i=="|": cbar+=1
            elif i=="*" and cbar%2==0: c+=1
        return c