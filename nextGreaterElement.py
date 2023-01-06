class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            for j in range(len(nums2)):
                if i==nums2[j]:
                    if j==len(nums2)-1:
                        ans.append(-1)
                        break;
                    else:
                        j+=1
                        c=False
                        while j<len(nums2):
                            if nums2[j]>i:
                                c=True
                                break
                            else:
                                j+=1
                        if c:
                            ans.append(nums2[j])
                            break
                        else:
                            ans.append(-1)
                            break
        return ans
