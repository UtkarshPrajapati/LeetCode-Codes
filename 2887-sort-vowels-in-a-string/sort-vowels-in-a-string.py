class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"A","E","I","O","U","a","e","i","o","u"}
        v = deque(sorted([c for c in s if c in vowels]))
        return "".join([v.popleft() if c in vowels else c for c in s])