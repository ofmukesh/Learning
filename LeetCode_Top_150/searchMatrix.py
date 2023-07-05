def find(arr,t):
    l=0
    r=len(arr)
    while l<r:
        mid=int((l+r)/2)
        if t==arr[mid]:
            return True 
        elif arr[l]<=t<=arr[mid]:
            r=mid
        else:
            l=mid+1
    return False
                

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0]:
            return False
        elif target>matrix[-1][-1]:
            return False
        else:
            l=0
            r=len(matrix)
            # first find the row where target may be found 
            while l<r:
                mid=int((l+r)/2)
                if matrix[l][0]<=target<=matrix[mid][-1]:
                    r=mid
                else:
                    l=mid+1
            check=find(matrix[l],target) if l<len(matrix) else False # checking the target is exist in the row or not 
            return check
