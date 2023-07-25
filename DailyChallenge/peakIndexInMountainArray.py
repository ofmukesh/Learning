#1
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        prev=0
        curr=1
        # itrate while i < i+1
        while arr[curr]>arr[prev]:
            prev+=1
            curr+=1
        
        return prev
        # T.C -> O(N)
        # S.C -> O(1)

#2
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
        # T.C -> O(log(n))
        # S.C -> O(1)
