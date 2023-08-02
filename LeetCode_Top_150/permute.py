class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,path):
            if not nums: # if the nums array is empty then add the path(new arr) to results
                results.append(path)

            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        
        results=[]
        backtrack(nums,[])
        return results
