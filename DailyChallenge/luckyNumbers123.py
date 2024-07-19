class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])

        rowsMins={}
        for i in range(rows):
            j=0
            minIdx=j
            currMin=matrix[i][j]

            while j < len(matrix[i]):
                if matrix[i][j] < currMin:
                    currMin=matrix[i][j]
                    minIdx=j
                j+=1
            
            rowsMins[matrix[i][minIdx]]=[i,minIdx]
        
        colsMaxs={}
        for j in range(cols):
            i=0
            maxIdx=i
            currMax=matrix[i][j]

            while i < len(matrix):
                if matrix[i][j] > currMax:
                    currMax=matrix[i][j]
                    maxIdx=i
                i+=1
            
            colsMaxs[matrix[maxIdx][j]]=[maxIdx,j]

        ans=[]

        for row in rowsMins.keys():
            if colsMaxs.get(row):
                if rowsMins[row] == colsMaxs[row]:
                    ans.append(row)

        return ans
