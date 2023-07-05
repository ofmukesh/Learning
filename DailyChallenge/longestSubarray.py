# Initial Solution
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) and nums[i] == 0:  # Skip leading zeros
            i += 1

        if i == len(nums):
            return 0  # If all elements are zeros, return 0

        max_count = 0
        count = 0
        del_idx = 0 if i == 0 else i - 1  # Index of the last deleted zero
        rem_del = 1 if i == 0 else 0  # Flag to indicate if one zero can be deleted
        while i < len(nums):
            if nums[i] == 1:
                i += 1
                count += 1  # Increment count for consecutive ones
            elif nums[i] == 0 and rem_del == 1:
                rem_del = 0
                del_idx = i
                i += 1
                # If a zero is encountered and one deletion is allowed,
                # update the deletion index and reset the flag and count
            elif nums[i] == 0 and rem_del == 0:
                i = del_idx + 1
                rem_del = 1
                count = 0
                # If a zero is encountered and no deletion is allowed,
                # move the pointer to the next index after the last deleted zero
                # and reset the flag and count
            max_count = max(max_count, count)  # Update the maximum count
        
        if rem_del == 1:
            max_count -= 1
            # If one deletion is still allowed at the end, decrement the maximum count by 1

        return max_count  # Return the longest subarray length


# Optimized Solution
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = l = 0  # Initialize count and left pointer (l) to zero
        
        for r in nums:
            if not r:
                count += 1  # Increment count for consecutive zeros
            if count > 1:
                if not nums[l]:
                    count -= 1
                l += 1
                # If count exceeds 1, move the left pointer to the right until
                # the count of zeros becomes valid (at most one deletion allowed)
    
        return len(nums) - l - 1
        # Return the length of the subarray by subtracting the left pointer from
        # the total length of the array and subtracting 1 (to account for the zero
        # at the left pointer position)
