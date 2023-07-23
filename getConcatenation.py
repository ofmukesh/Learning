class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for num in nums[:n]:
            nums.append(num)
        return nums

        # Time complexity - O(n)
        # Space complexity - O(1)
