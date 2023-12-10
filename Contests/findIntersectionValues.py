class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_nums1={}
        for num in nums1:
            dict_nums1[num]=1
            
        dict_nums2={}
        for num in nums2:
            dict_nums2[num]=1
        
        val1=0
        for num in nums1:
            if dict_nums2.get(num):
                val1+=1
        
        val2=0
        for num in nums2:
            if dict_nums1.get(num):
                val2+=1
        
        return [val1,val2]
        
