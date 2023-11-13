class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"A","E","I","O","U","a","e","i","o","u"}
        v = [c for c in s if c in vowels]
        heapq.heapify(v)
        return "".join([heapq.heappop(v) if c in vowels else c for c in s])