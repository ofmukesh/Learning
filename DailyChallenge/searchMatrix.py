class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        e=len(matrix)
        while i<e:
            mid=(e+i)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                return self.binarySearch(matrix[mid],target)
            elif target<matrix[mid][0]:
                e=mid
            else:
                i=mid+1
        return False
    
    def binarySearch(self,arr,t):
        l=0
        r=len(arr)

        while l<r:
            mid=(r+l)//2
            if arr[mid]==t:
                return True
            elif t<arr[mid]:
                r=mid
            else:
                l=mid+1
        
        return False
