def squareOfNum(n):
    str_of_n=str(n)
    sum_of_squares=0
    for num_c in str_of_n:
        sum_of_squares+=(int(num_c)**2)
    if sum_of_squares>6:
        return squareOfNum(sum_of_squares)
    else:
        return sum_of_squares

class Solution:
    def isHappy(self, n: int) -> bool:
        if squareOfNum(n)==1:
            return True
        return False
