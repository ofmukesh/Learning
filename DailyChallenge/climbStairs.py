class Solution:
    def climbStairs(self, n: int) -> int:
        pre, cur = 0,1
        for i in range(n):
            pre, cur = cur, pre+cur
        return cur
        



'''
# recusive with DP memoization
def climbStairs(self, n: int) -> int:
        def stairs(n,dp):
            if dp[n]!=-1:
                return dp[n]
                
            if n<0:
                return 0
                
            if n==0:
                return 1
            
            dp[n] = stairs(n-1,dp)+stairs(n-2,dp)
            
            return dp[n]
        
        dp=[-1]*(n+1)
        return stairs(n,dp)
'''



'''
# recusive solution
class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(n):
            if n<0:
                return 0
                
            if n==0:
                return 1
            
            return stairs(n-1)+stairs(n-2)
        return stairs(n)
'''
