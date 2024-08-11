class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color==image[sr][sc]: return image
        
        rpColor=image[sr][sc]
        def rec(i,j):
            if i<0 or i>=len(image) or j<0 or j>=len(image[i]):
                return
            if image[i][j] != rpColor:
                return 
            image[i][j]=color
            rec(i+1,j)
            rec(i,j+1)
            rec(i-1,j)
            rec(i,j-1)
            return 
        rec(sr,sc)
        return image
