class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrackUnique(nums,path):
            if not nums:
                results.append(path)
                return
            i=0
            while i < len(nums):
                backtrackUnique(nums[:i]+nums[i+1:],path+[nums[i]])
                while i<len(nums)-1 and nums[i] == nums[i+1]:
                    i+=1
                i+=1

        results=[]
        backtrackUnique(nums,[])
        return results
