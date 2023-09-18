class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            row=mat[i]
            count=0
            for sol in row:
                count+=sol
            mat[i]=(count,i)
        mat=sorted(mat)

        return [row[1] for row in mat[:k]]
