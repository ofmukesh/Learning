class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        p = 0
        sign = 1
        total = 0
        while p < len(s):
            char = s[p]
            if char.isdigit():
                num = 0
                while p < len(s) and s[p].isdigit():
                    num = num*10 + int(s[p])
                    p += 1
                p -= 1
                num *= sign
                total += num
                sign = 1
            elif char == '(':
                stack.append(total)
                stack.append(sign)
                total, sign = 0, 1
            elif char == ')':
                total *= stack.pop()
                total += stack.pop()
            elif char == '-':
                sign = -1
            p += 1
        return total
