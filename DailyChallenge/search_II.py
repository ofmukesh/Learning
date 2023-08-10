class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0;
        r=len(nums)-1;

        # if array is 0 times rotated and ele is not exist in arrayreturn -1
        if nums[l]<nums[r] and (nums[l]>target or nums[r]<target):
            return False

        while l <= r:
            mid=int((l+r)/2);

            if nums[mid] == target:
                return True
            
            # skip duplicates
            if nums[l]==nums[mid] and nums[mid]==nums[r]:
                while l <= r and nums[l]==nums[mid] and nums[mid]==nums[r]:
                    l+=1
                    r-=1
            elif nums[l]<=nums[mid]:
                if target>nums[mid] or nums[l]>target:
                    l=mid+1;
                else:
                    r=mid-1
            else:
                if target<nums[mid] or nums[r]<target:
                    r=mid-1
                else:
                    l=mid+1;

        return False;
             
