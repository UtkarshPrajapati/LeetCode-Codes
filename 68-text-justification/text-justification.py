class Solution:
    def fullJustify(self,words, maxWidth):
        res, cur, num = [], [], 0
        for w in words:
            if num + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num = [], 0
            cur += [w]
            num += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]