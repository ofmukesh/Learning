class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[ k for k in range(n)]
        count=0
        for i in range(2,len(prime)):
            if prime[i]:
                for j in range(i*2,len(prime),+i):
                    prime[j]=False
                count+=1
            print(prime)
        return count 
