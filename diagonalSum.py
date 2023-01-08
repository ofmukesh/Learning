class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)==1:
            return sum(mat[0])
        elif len(mat)==2:
            return (sum(mat[0])+sum(mat[1]))
        else:
            s=0
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if i==j:
                        s+=mat[i][j];
                    elif j==len(mat)-1-i:
                        s+=mat[i][j];
            return s
