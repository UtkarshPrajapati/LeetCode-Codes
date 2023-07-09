class Solution:
    def largestVariance(self, s: str) -> int:
        result,count,index = 0,defaultdict(int),defaultdict(list)
        for i,ch in enumerate(s):
            count[ch] += 1
            index[ch].append((i, ch))
        for a, b in itertools.permutations(count.keys(), 2):
            total, flag = 0, False
            if count[b] - 1 > result:
                for _, x in sorted(index[a] + index[b]):
                    if x == a and (flag := total > 0): total -= 1
                    elif x == b:
                        result = max(result, total + flag)
                        total += 1
        return result
        