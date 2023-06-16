class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1  # Initialize two pointers, left and right, pointing to the start and end of the list respectively.

        while left < right:  # Continue the loop until the pointers meet or cross each other.
            if numbers[left] + numbers[right] == target:  # If the sum of the numbers at the left and right pointers is equal to the target:
                return [left + 1, right + 1]  # Return the indices (1-based) of the two numbers that add up to the target.
            
            if numbers[left] + numbers[right] < target:  # If the sum is less than the target:
                left += 1  # Move the left pointer to the right, increasing its index.
            else:  # If the sum is greater than the target:
                right -= 1  # Move the right pointer to the left, decreasing its index.
