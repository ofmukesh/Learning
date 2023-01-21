class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        c=(set(nums1)&set(nums2))
        if len(c)==0:
            return -1;
        return min(set(nums1)&set(nums2))
    
