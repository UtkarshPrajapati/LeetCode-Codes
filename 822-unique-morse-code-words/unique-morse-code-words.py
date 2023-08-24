class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set("".join([".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."][ord(i)-97] for i in w) for w in words))