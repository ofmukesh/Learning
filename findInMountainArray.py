# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        # find the index of the peak element

        s = 0
        e = mountain_arr.length()-1

        while s<e:
            mid = s + (e-s)//2
            x = mountain_arr.get(mid)
            y = mountain_arr.get(mid+1)
            if x>y:
                e = mid
            else:
                s  = mid+1
        temp = s

        # first search for the target element in Ascending Slope of Mountain i.e. elements on the left of the peak

        s = 0
        e = temp
        while s<=e:
            mid  = s+ (e-s)//2
            x = mountain_arr.get(mid)
            if x<target:
                s = mid+1
            elif x==target:
                return mid
            else:
                e = mid-1

        # then search for the target element in Descending Slope of Mountain i.e. elements on the right of the peak if target is not present on the left side

        s = temp
        e = mountain_arr.length()-1
        while s<=e:
            mid  = s+ (e-s)//2
            x = mountain_arr.get(mid)
            if x<target:
                e = mid-1
            elif x==target:
                return mid
            else:
                s = mid+1

        # if no such element present

        return -1
