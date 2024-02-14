class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initializing an answer array of size n
        ans = [0] * n

        # Initializing two pointers to track even and
        # odd indices for positive and negative integers respectively
        pos_index, neg_index = 0, 1

        for i in range(n):
            if nums[i] > 0:
                # Placing the positive integer at the
                # desired index in ans and incrementing pos_index by 2
                ans[pos_index] = nums[i]
                pos_index += 2
            else:
                # Placing the negative integer at the
                # desired index in ans and incrementing neg_index by 2
                ans[neg_index] = nums[i]
                neg_index += 2

        return ans

'''
# TLE
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        f=1 # flag that which type of integer is required (positive/negative)
        i=0
        while i<len(nums):
            if nums[i]>0 and f==1: f=-1
            elif nums[i]<0 and f==-1: f=1
            elif nums[i]>0 and f==-1:
                j=i
                while j<len(nums) and nums[j]>0:
                    j+=1
                if j<len(nums):
                    nums.insert(i,nums.pop(j))
                    i+=1
            elif nums[i]<0 and f==1:
                j=i
                while j<len(nums) and nums[j]<0:
                    j+=1
                if j<len(nums):
                    nums.insert(i,nums.pop(j))
                    i+=1
            i+=1
        
        return nums
'''
