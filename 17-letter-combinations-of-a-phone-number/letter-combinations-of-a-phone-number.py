class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits: return [''.join(x) for x in product(*list([None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"][int(n)] for n in digits))]
        return [] 