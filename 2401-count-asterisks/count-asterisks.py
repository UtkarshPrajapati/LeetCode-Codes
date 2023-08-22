class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(i=="*" and s[:j].count("|")%2==0 for j,i in enumerate(s))