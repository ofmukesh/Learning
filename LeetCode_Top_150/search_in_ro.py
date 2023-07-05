class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0;
        r=len(nums)-1;

        # if array is 0 times rotated and ele is not exist in arrayreturn -1
        if nums[l]<nums[r] and (nums[l]>target or nums[r]<target):
            return -1

        while l <= r:
            mid=int((l+r)/2);

            # if mid element is the target return simply its index
            if nums[mid] == target:
                return mid;
            # if (l to mid-1) is sorted 
            elif nums[l]<=nums[mid]:
                if target>nums[mid] or nums[l]>target:
                    l=mid+1;
                else:
                    r=mid-1
            # if (mid+1 to r) is sorted
            else:
                if target<nums[mid] or nums[r]<target:
                    r=mid-1
                else:
                    l=mid+1;
        return -1;
             
