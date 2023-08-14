class Solution:
    def moveZeroes(self,a):
        i,c=0,0
        while i<len(a):
            if a[i]==0: a.pop(i);c+=1
            else: i+=1
        a.extend([0]*c)