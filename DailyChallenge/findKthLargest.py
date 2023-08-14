import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)
    
    def quick_select(self, nums, left, right, k):
        if left == right:
            return nums[left]
        
        pivot_idx = left + random.randint(0, right - left)
        pivot_idx = self.partition(nums, left, right, pivot_idx)
        
        if pivot_idx == k:
            return nums[pivot_idx]
        elif pivot_idx < k:
            return self.quick_select(nums, pivot_idx + 1, right, k)
        else:
            return self.quick_select(nums, left, pivot_idx - 1, k)
    
    def partition(self, nums, left, right, pivot_idx):
        pivot_value = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        return store_idx
