class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result=0
        merged=[]
        length=len(nums1)+len(nums2)

        for i in range(length):
            if len(nums1)==0:
                merged.append(nums2[0])
                nums2.pop(0)
            elif len(nums2)==0:
                merged.append(nums1[0])
                nums1.pop(0)
            elif nums1[0]<=nums2[0]:
                merged.append(nums1[0])
                nums1.pop(0)
            elif nums2[0]<nums1[0]:
                merged.append(nums2[0])
                nums2.pop(0)
        if length%2==0:
            result=(merged[int(length/2)-1]+merged[int(length/2)])/2
        else:
            result=merged[int(length/2)]
        return result
