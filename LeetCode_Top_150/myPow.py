class Solution:
    def myPow(self, x: float, n: int) -> float:
        # If n is negative, we need to calculate 1 / x^n
        if n < 0:
            x = 1/x
            n = abs(n)
            
        # Initialize a variable to store the result
        ans = 1

        # Exponentiation by squaring algorithm
        while n:
            # Check if the least significant bit of n is set (n is odd)
            if n & 1:
                ans *= x   # Multiply the result by x if n is odd

            x *= x       # Square x for the next iteration (x^(2^i))
            n //= 2      # Halve n (integer division) for the next iteration (2^i)

        # Return the final result
        return ans
