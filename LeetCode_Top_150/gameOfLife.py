class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for row in range(len(board)):
            for col in range(len(board[row])):
                # count of live neighbors of current cell
                total_neighbors = 0

                # current cell
                curr=board[row][col]

                # vertical and horizontal neighbors 
                left=board[row][col-1] if col>0 else 0
                right=board[row][col+1] if col<len(board[row])-1 else 0
                top=board[row-1][col] if row>0 else 0
                bottom=board[row+1][col] if row<len(board)-1 else 0

                # add counts of vertical and horizontal neighbors to total_neighbors
                # cell>1 refers to updated state
                total_neighbors+=1 if 0<left<=2 else 0
                total_neighbors+=1 if 0<right<=2 else 0
                total_neighbors+=1 if 0<top<=2 else 0
                total_neighbors+=1 if 0<bottom<=2 else 0

                # diagonal neighbors 
                top_left=board[row-1][col-1] if row>0 and col>0 else 0
                top_right=board[row-1][col+1] if row>0 and col<len(board[row])-1 else 0
                bottom_left=board[row+1][col-1] if row<len(board)-1 and col>0 else 0
                bottom_right=board[row+1][col+1] if row<len(board)-1 and col<len(board[row])-1 else 0

                # add counts of diagonal neighbors to total_neighbors
                # cell>1 refers to updated state
                total_neighbors+=1 if 0<top_left<=2 else 0
                total_neighbors+=1 if 0<top_right<=2 else 0
                total_neighbors+=1 if 0<bottom_left<=2 else 0
                total_neighbors+=1 if 0<bottom_right<=2 else 0

                # set to 2 for die and 3 for live
                if curr==1 and (total_neighbors<2 or total_neighbors>3):
                    board[row][col]=2
                elif curr==0 and total_neighbors==3:
                    board[row][col]=3   
       
        # updating the board to next generation state
        for row in range(len(board)):
            for col in range(len(board[row])):
                curr=board[row][col]
                
                if curr==3:
                    board[row][col]=1
                elif curr==2:
                    board[row][col]=0

















