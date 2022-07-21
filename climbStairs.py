class Solution:
    def climbStairs(self, n: int) -> int:
        ans=0;
        i=1;
        x=[0,1]
        while i<=n:
            ans=x[0]+x[1]
            x[0]=x[1]
            x[1]=ans
            i=i+1;
        return ans
