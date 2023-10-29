class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(i=0, total=0, last=0, expr='', ans=set()):
            if i == len(num) and total == target: ans.add(expr);return
            for j in range(i, len(num)):
                n = int(num[i:j+1])
                if i == 0: backtrack(j+1, n, n, str(n), ans)
                else:
                    backtrack(j+1, total + n, n, expr + '+' + str(n), ans)
                    backtrack(j+1, total - n, -n, expr + '-' + str(n), ans)
                    backtrack(j+1, total - last + last * n, last * n, expr + '*' + str(n), ans)
                if n == 0: break
            return list(ans)
        return backtrack()