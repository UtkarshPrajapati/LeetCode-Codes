class Solution:
    def generate(self, n: int) -> List[List[int]]:
        a,c=[[1],[1,1]],2
        if n<3: return a[:n]
        while c!=n:
            x=a[-1]
            a.append([1]+[x[i]+x[i+1] for i in range(c-1)]+[1])
            c+=1
        return a