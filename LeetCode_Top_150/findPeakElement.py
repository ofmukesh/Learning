class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0  # Initialize the left pointer to the start of the array
        j = len(nums) - 1  # Initialize the right pointer to the end of the array
        
        while i < j:  # Perform binary search until left and right pointers meet
            mid = int((i + j) / 2)  # Calculate the middle index
            
            if nums[mid] < nums[mid + 1]:  # If the element at mid is smaller than the next element
                i = mid + 1  # Move the left pointer to mid + 1
            else:
                j = mid  # Otherwise, move the right pointer to mid
                
        return i  # Return the index i as the peak element index
