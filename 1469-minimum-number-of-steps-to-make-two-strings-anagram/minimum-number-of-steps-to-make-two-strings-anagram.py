class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        steps = 0
        for char in counter_s:
            if char in counter_t:
                if counter_s[char] > counter_t[char]:
                    steps += counter_s[char] - counter_t[char]
            else: steps += counter_s[char]
        return steps