class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"A","E","I","O","U","a","e","i","o","u"}
        v = sorted([c for c in s if c in vowels])
        return "".join([v.pop(0) if c in vowels else c for c in s])