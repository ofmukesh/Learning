class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Remove any extra elements at the end of nums1 to make its length equal to m.
        while len(nums1) != m:
            nums1.pop()

        i = 0  # Pointer for nums1
        j = 0  # Pointer for nums2

        # Merge nums1 and nums2 in a sorted manner while comparing elements.
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1  # Increment i if the current element in nums1 is smaller.
            elif nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])  # Insert the current element from nums2 into nums1 at index i.
                j += 1  # Increment both i and j.
                i += 1
        
        # Add any remaining elements from nums2 to the end of nums1.
        while j < len(nums2):
            nums1.append(nums2[j])
            j += 1

        '''
        Time Complexity: O(m + n) in the worst case.
        Space Complexity: O(1).
        '''
