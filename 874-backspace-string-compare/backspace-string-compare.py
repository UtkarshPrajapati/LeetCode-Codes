class Solution:
    def backspaceCompare(self,s,t):
        def f(s):
            skip=0
            for x in reversed(s):
                if x=='#': skip+=1
                elif skip: skip-=1
                else: yield x
        return all(x==y for x,y in zip_longest(f(s),f(t)))