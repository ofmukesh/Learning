class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Ensure k is within the range of 0 to n.

        # Reverse the entire list.
        nums.reverse()
        
        # Reverse the first k elements.
        nums[:k] = reversed(nums[:k])
        
        # Reverse the remaining elements.
        nums[k:] = reversed(nums[k:])

# Time Complexity: O(n), where 'n' is the length of 'nums'.
# Space Complexity: O(1) - The function modifies 'nums' in-place without using any additional data structures.


'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            # Insert the last element of 'nums' at the beginning.
            nums.insert(0, nums[-1])
            # Remove the last element of 'nums'.
            nums.pop()

# Time Complexity: O(k * n), where 'k' is the number of rotations and 'n' is the length of 'nums'.
# Space Complexity: O(1) - The function modifies 'nums' in-place without using any additional data structures.
'''
