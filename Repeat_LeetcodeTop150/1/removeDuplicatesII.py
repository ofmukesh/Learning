class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2  # Initialize a pointer 'i' to start from the third element.
        
        while i < len(nums):
            # Check if the current element is a duplicate of the previous two elements.
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums.pop(i)  # Remove the current element at index 'i' if it's a duplicate.
            else:
                i += 1  # If the current element is not a duplicate, increment 'i' to move to the next element.

        # At this point, duplicates have been removed, and 'i' represents the length of the modified list.
        return len(nums)

# Time Complexity: O(n), where 'n' is the length of the 'nums' list. In the worst case, we may iterate through all elements once.
# Space Complexity: O(1) - The function modifies the 'nums' list in-place without using any additional data structures.


'''
# 2 Solution 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        frq = {}  # Initialize a dictionary 'frq' to store element frequencies.

        i = 0  # Initialize a pointer 'i' to keep track of the current index.

        while i < len(nums):
            if frq.get(nums[i]) and frq[nums[i]] >= 2:
                # If the element already appears twice or more, remove it from 'nums'.
                del nums[i]
            else:
                # Otherwise, update the frequency count in 'frq' and increment 'i'.
                frq[nums[i]] = 1 + frq.get(nums[i], 0)
                i += 1

        # At this point, duplicates have been removed, and 'i' represents the length of the modified list.
        # You should return the length of the modified list here.
        return len(nums)
'''
