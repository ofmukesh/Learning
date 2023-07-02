class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            is_negative = True
            x = abs(x)
        else:
            is_negative = False

        reversed_num = 0

        while x != 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit

            if reversed_num > 2**31 - 1:
                return 0

            x = x // 10

        if is_negative:
            reversed_num *= -1

        return reversed_num
