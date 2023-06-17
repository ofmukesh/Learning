class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}

        for idx,val in enumerate(nums):
            if temp.get(target-val)!=None:
                return [temp[target-val],idx]
            else:
                temp[val]=idx
