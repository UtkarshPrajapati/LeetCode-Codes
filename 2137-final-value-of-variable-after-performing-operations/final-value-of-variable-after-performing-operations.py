class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([-1,1][i in ["++X", "X++"]] for i in operations)