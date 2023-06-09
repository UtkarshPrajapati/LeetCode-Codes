class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i=0;n=len(letters)
        while i<n and letters[i]<=target: i+=1
        return letters[i] if i<n else letters[0]