class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        opts=0 # intial operations
        smallest=min(nums) # smallest element of nums
        nums.sort(reverse=True) # sorting array nums in deceasing order

        # itrating nums array
        for i in range(len(nums)):
            if nums[i]==smallest: # if array elements are equal
                break
            if nums[i]==nums[i+1]: # if elements are same then skip 
                continue
            else:
                opts += i+1 # adding operations ( we are adding new i+1 operations but why i+1, bcz all the previous elements also reduces into nextLargest element )
        return opts
        
        # time complexity -> O(n log n)
        # space complexity -> o(1)
