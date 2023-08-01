class Solution:
    def sortSentence(self, s: str) -> str:
        x=s.split(" ")
        l=[""]*len(x)
        for i in x:
            l[int(i[-1])-1]=i[:len(i)-1]
        return " ".join(l)