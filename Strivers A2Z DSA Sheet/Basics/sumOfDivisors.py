#User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
    	if N <= 0:
          return 0
        div_sum = 0
            
        for i in range(1, N + 1):
          k = N // i
          div_sum += i * k
        
        return div_sum
