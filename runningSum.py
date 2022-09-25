class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_arr=0
        new_arr=[]
        for i in nums:
            sum_arr+=i
            new_arr.append(sum_arr)
        return new_arr
            
        
