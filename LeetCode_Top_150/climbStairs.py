# memorization is the simpliest way to solve the question -> get the ways for 3rd stair using its prev and 2nd prev stair possible distinct ways sum
# let's see -> if we have n=5 stairs & marco is going to reach the top

# on stair (n=5)      ways to reach top        
#   5 (n)                    1
#   4 (n-1)                  1
#   3 (n-2)                  2
#   2 (n-3)                  3
#   1 (n-4)                  5
#   0 (n-5)                  8

# see the chart if marco on nth stair he have 1 way & if marco start from n-1(4rth) stair he have 1 way to reach the top & if marco start from n-2(3rd) stair he have 2 ways to  reach the top 
# if u noticed-> to reach top from 3rd stair he have 2 ways , it's look like the sum of 5th and 4rth stair ways
# same at 3nd stair he have 3 ways , the sum of 4th and 3rth stair ways
# so looking at the cases we can solve the question using memorization last 2 stair ways and sum these to find ways to reach the top


# ---------------------code----------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        last=1
        last_one=1

        for i in range(n-1):
            last_one+=last
        
        return last_one
