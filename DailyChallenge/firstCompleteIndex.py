class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # store elements row and col idx in hashmap
        elements={}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                elements[mat[i][j]]=[i,j]
        
        # store counting of elments of each rows and cols 
        rows={}
        for i in range(len(mat)):
            rows[i]=len(mat[i])
        cols={}
        for i in range(len(mat[0])):
            cols[i]=len(mat)
        
        # now go through each index ian arr
        for idx,val in enumerate(arr):
            # get current element row and col idx
            row=elements[val][0]
            col=elements[val][1]

            rows[row]=rows[row]-1
            cols[col]=cols[col]-1

            if rows[row]==0: return idx
            if cols[col]==0: return idx

        return 0

        # time complexity :- O(m*n)
        # space complexity :- O(m+n)
