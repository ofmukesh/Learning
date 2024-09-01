class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res=[]

        if not len(original)==m*n: return res
        
        currIdx=0
        for i in range(m):
            for j in range(n):
                if j==0:
                    res.append([original[currIdx]])
                else:
                    res[-1].append(original[currIdx])
                currIdx+=1
        
        return res
