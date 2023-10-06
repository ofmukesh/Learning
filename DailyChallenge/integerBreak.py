class Solution:
    def integerBreak(self, n: int) -> int:
        # If n is less than or equal to 3, we can't break it further,
        # so return (n - 1).
        if n <= 3:
            return n - 1
        
        # If n is divisible by 3, we can break it into equal parts of 3.
        if n % 3 == 0:
            # Calculate the number of equal parts and return the product of these parts.
            return 3 ** (n // 3)
        
        # If n leaves a remainder of 1 when divided by 3,
        # we break it into two parts of 2 and one part of 3.
        if n % 3 == 1:
            # Calculate the number of equal parts of 3 and one part of 2, then return the product.
            return 3 ** (n // 3 - 1) * 4
        
        # If n leaves a remainder of 2 when divided by 3,
        # we break it into equal parts of 3 and one part of 2.
        if n % 3 == 2:
            # Calculate the number of equal parts of 3 and one part of 2, then return the product.
            return 3 ** (n // 3) * 2
