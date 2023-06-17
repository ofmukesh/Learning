class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[];
        nums.sort();

        for i,val in enumerate(nums):
            # skip if ele is equal to prev ele
            if i>0 and val==nums[i-1]:
                continue;  

            # now finding two more unique elements ( sum of these 3 elements = 0 )
            l=i+1;
            r=len(nums)-1;

            while l<r:
                # move right index pointer to prev ele if 3sum is bigger then 0, means need to sum with a negative element
                if nums[l]+nums[r]+val>0:
                    r-=1;
                # move left index pointer to prev ele if 3sum is bigger then 0, means need to sum with a negative element
                elif nums[l]+nums[r]+val<0:
                    l+=1;
                else:
                    # add 3 ele as subarray of answer array if sum of these ele is 0
                    res.append([val,nums[l],nums[r],]);
                    l+=1;
                    # skip if left ele is equal to left-1 ele
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
        return res;
