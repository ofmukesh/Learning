class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # return False if given num is less then 0 
            return False

        reversed_num = 0
        temp = x # storing original value to temp variable 

        while temp != 0:
            digit = temp % 10 # extracting last digit from temp
            # multiplying reversed num by 10 then adding the digit to reversed num
            reversed_num = reversed_num * 10 + digit 
            temp //= 10 # removing last digit from temp

        return reversed_num == x # if reversed_num is equal to temp return True else False
