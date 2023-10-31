class Solution:
    def countPrimes(self,n):
        if n<2: return 0
        primes=[False]*2+[True]*(n-2)
        p=2
        while p*p<n:
            if primes[p]==True:
                for i in range(p*p,n,p):
                    primes[i] = False
            p+=1
        return sum(i for i in primes)