class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Initialize a pointer 'i' to keep track of the current index.
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)  # Remove the element at index 'i' if it matches 'val'.
            else:
                i += 1  # Increment 'i' to move to the next element.

        # At this point, all occurrences of 'val' have been removed, and 'i' represents the length of the modified list.
        return len(nums)

# Time Complexity: O(n), where 'n' is the length of the 'nums' list. In the worst case, we may iterate through all elements once.
# Space Complexity: O(1) - The function modifies the 'nums' list in-place without using any additional data structures.
