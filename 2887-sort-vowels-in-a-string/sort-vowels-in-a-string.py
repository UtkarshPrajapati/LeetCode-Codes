class Solution:
    def sortVowels(self, s: str) -> str:
        n=len(s)
        s1=[""]*n
        vowels={"A","E","I","O","U","a","e","i","o","u"}
        v=[]
        for i in range(n):
            if s[i] not in vowels: s1[i]=s[i]
            else: v.append(s[i])
        v.sort()
        for i in range(n):
            if s1[i]=="": s1[i]=v.pop(0)
        return "".join(s1)