class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c,s=Counter(chars),0
        for i in words:
            if Counter(i)<=c: s+=len(i)
        return s