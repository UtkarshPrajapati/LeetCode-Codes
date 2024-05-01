class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=None
        for i,cha in enumerate(word):
            if ch==cha: a=i;break
        if not a: return word
        return word[:a+1][::-1]+word[a+1:]