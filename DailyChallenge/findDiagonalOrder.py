class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = deque([(0, 0)])
        
        while q:
            # remove current row,col from deque and append thier values in result (res)
            row, col = q.popleft() 
            res.append(nums[row][col])

            # if there is row after current
            if col == 0 and row + 1 < len(nums):
                q.append((row + 1, 0))
            
            # if there is col after current
            if col + 1 < len(nums[row]):
                q.append((row, col + 1))
        # return the result array 
        return res
