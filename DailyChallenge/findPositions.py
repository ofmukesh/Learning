class Solution:
    def binarySearch(self, nums, target):
        # Initialize left and right pointers.
        l = 0
        r = len(nums) - 1

        # Perform binary search.
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid  # Return the index if the target is found.
            elif nums[mid] < target:
                l = mid + 1  # Adjust the left pointer if the target is greater.
            else:
                r = mid - 1  # Adjust the right pointer if the target is smaller.

        return -1  # Return -1 if the target is not found.

    def findPositions(self, nums, target, idx):
        idx2 = idx + 1

        # Find the leftmost index of the target.
        while idx >= 0 and nums[idx] == target:
            idx -= 1

        # Find the rightmost index of the target.
        while idx2 < len(nums) and nums[idx2] == target:
            idx2 += 1

        return [idx + 1, idx2 - 1]  # Return the range of positions where the target is found.

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ele_idx = self.binarySearch(nums, target)

        if ele_idx == -1:
            return [-1, -1]  # If the target is not found, return [-1, -1].
        else:
            ele_positions = self.findPositions(nums, target, ele_idx)
            return ele_positions  # Return the range of positions where the target is found.
