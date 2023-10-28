class Solution:
    def countVowelPermutation(self, n):
        MOD,a,e,i,o,u=1000000007,1,1,1,1,1
        for _ in range(n-1):
            a,e,i,o,u=(e+i+u)%MOD,(a+i)%MOD,(e+o)%MOD,i%MOD,(i+o)%MOD
        return (a+e+i+o+u)%MOD