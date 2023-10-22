class Solution:
    def is_valid_assignment(self, x, count):
        for curr, temp in count.items():
            left = temp % x
            total = temp // x

            if left < x - 1:
                required = (x - 1) - left
                if total >= required:
                    left = x - 1

            if 0 < left < x - 1:
                return False

        return True

    def minGroupsForValidAssignment(self, nums):
        maxi = 0
        n = len(nums)

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            maxi = max(maxi, count[num])

        for i in range(maxi, 0, -1):
            if self.is_valid_assignment(i, count):
                res = 0
                for curr, temp in count.items():
                    left = temp % i
                    res += temp // i
                    if left > 0:
                        res += 1
                return res

        return -1
