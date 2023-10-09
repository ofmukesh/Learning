class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1  # Initialize a pointer 'i' to start from the second element.
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)  # Remove the current element at index 'i' if it's a duplicate of the previous element.
            else:
                i += 1  # If the current element is not a duplicate, increment 'i' to move to the next element.

        # At this point, duplicates have been removed, and 'i' represents the length of the modified list.
        return len(nums)

# Time Complexity: O(n), where 'n' is the length of the 'nums' list. In the worst case, we may iterate through all elements once.
# Space Complexity: O(1) - The function modifies the 'nums' list in-place without using any additional data structures.

'''
#2 Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = {}  # Initialize a dictionary 'temp' to store unique elements and their counts.
        i = 0  # Initialize a pointer 'i' to keep track of the current index.

        while i < len(nums):
            num = nums[i]  # Get the current element.

            if temp.get(num) is not None:
                # If the element already exists in 'temp' (i.e., it's a duplicate), remove it from 'nums'.
                del nums[i]
            else:
                # If the element is not a duplicate, add it to 'temp' with a count of 1 and increment 'i'.
                temp[num] = 1
                i += 1

        # At this point, duplicates have been removed, and 'i' represents the length of the modified list.
        return len(nums)

# Time Complexity: O(n), where 'n' is the length of the 'nums' list. In the worst case, we may iterate through all elements once.
# Space Complexity: O(k), where 'k' is the number of unique elements in 'nums'. The 'temp' dictionary stores unique elements.
'''
