class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict={}
        if len(nums)==2:
            return [0,1]
        for i in range(len(nums)):
            if nums_dict.get(target-nums[i])!=None:
                return [nums_dict.get(target-nums[i]),i];
            else:
                nums_dict[nums[i]]=i;
