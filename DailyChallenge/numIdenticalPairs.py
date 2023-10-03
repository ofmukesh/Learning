class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0
        
        for num in nums:
            if num in count:
                result += count[num]
                count[num] += 1
            else:
                count[num] = 1
        
        return result


        # ans=0
        # for i in range(len(nums)):
        #     a=nums[i]
        #     for b in nums[i+1:]:
        #         if a==b:
        #             ans+=1
        # return ans
    # Time Complexity -> O(n^2)
    # Space Complexity -> O(1)

