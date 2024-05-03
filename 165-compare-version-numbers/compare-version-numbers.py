class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        l1,l2=map(int,v1.split(".")),map(int,v2.split("."))
        for i,j in zip_longest(l1,l2,fillvalue=0):
            if i>j: return 1
            elif i<j: return -1
        return 0