class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l=0
        for i in range(len(nums)-1-l):
            if nums[i]==nums[i+1] and nums[i]!=0:
                nums[i]+=nums[i+1]
                nums[i+1]=0;
                i-=1
                l+=1
        i=0;
        l=0;
        while i<len(nums)-l:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                l+=1
            else:
                i+=1
                
        
        return nums
# Link https://leetcode.com/contest/weekly-contest-318/problems/apply-operations-to-an-array/
