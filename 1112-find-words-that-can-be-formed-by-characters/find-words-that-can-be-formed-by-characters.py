class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s=0
        for i in words:
            for j in i:
                if chars.count(j)<i.count(j): break
            else: s+=len(i)
        return s