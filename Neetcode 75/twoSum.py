class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}

        for idx,num in enumerate(nums):
            data[num]=idx
        
        for idx,num in enumerate(nums):
            if data.get(target-num)!=None and data.get(target-num)!=idx:
                return [min(data[target-num],idx),max(data[target-num],idx)]
        
        return [-1,-1]
