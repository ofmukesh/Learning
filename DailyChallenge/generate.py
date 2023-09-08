class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(1,numRows):
            new=[1]*(i+1)
            for j in range(len(new)):
                val = ans[i-1][j-1] if j-1>=0 else 0
                val += ans[i-1][j] if j<len(ans[i-1]) else 0
                new[j]=val
            ans.append(new)
        return ans
