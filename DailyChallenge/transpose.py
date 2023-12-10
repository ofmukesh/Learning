class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[] # storing transpose matrix
        for j in range(len(matrix[0])): # j defined as col of the metrix
            tmp=[]
            for i in range(len(matrix)): # itrating all the rows of matrix
                tmp.append(matrix[i][j]) # appending element to tmp 
            ans.append(tmp) # append new row to tranpose matrix (ans)
        
        return ans # return transpose array

'''
Complexity Analysis

Time Complexity: O(R∗C), where R and C are the number of rows and columns in the given matrix A.

Space Complexity: O(R∗C), the space used by the answer.
'''
