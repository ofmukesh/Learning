class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]

        for num in nums:
            left.append(num*left[-1])
        left.pop()

        right=[1]
        for i in range(len(nums)-1,0,-1):
            right.append(nums[i]*right[-1])

        ans=[]
        for i in range(len(nums)):
            ans.append(left[i]*right[len(nums)-1-i])

        return ans
