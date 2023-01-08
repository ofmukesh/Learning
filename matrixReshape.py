class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)==r and c/r==len(mat[0]) or r*c!=len(mat)*len(mat[0]):
            return mat
        else:
            arr=[[]]
            index=0
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if c==len(arr[index]):
                        arr.append([])
                        index+=1                        
                    arr[index].append(mat[i][j])
            return arr
            
