# sort the array and add element to array if satisfy the conditions else return []
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res=[]

        # sorting the array
        nums.sort()

        for i in range(0,len(nums),3): # iterate three element at every time
            if nums[i+1]-nums[i]<=k and nums[i+2]-nums[i]<=k and nums[i+2]-nums[i+1]<=k:
                res.append([nums[i],nums[i+1],nums[i+2]]) # add to result array if conditions met
            else:
                return [] # return empty array if elements not satisfied the given conditions
        
        return res # return result array 
