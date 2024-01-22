class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                errorDupNum=nums[i]
                nums.pop(i)
                break
        
        for num in range(1,len(nums)+2):
            if num-1<len(nums) and num != nums[num-1]:
                errorNum=num
                break
            errorNum=num

        return [errorDupNum,errorNum]
