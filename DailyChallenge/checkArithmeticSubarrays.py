class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_arithmetic(sub):
            sub.sort()
            diff = sub[1] - sub[0]
            for i in range(2, len(sub)):
                if sub[i] - sub[i - 1] != diff:
                    return False
            return True

        res = []
        for q in range(len(l)):
            res.append(is_arithmetic(nums[l[q]:r[q]+1]))
        return res
