class Solution:
    def sequentialDigits(self, low, high):
        c = "123456789"
        a = []

        for i in range(len(c)):
            for j in range(i + 1, len(c) + 1):
                curr = int(c[i:j])
                if low <= curr <= high:
                    a.append(curr)

        a.sort()
        return a

