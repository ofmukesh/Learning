class Solution:
    def memoSol(self,memo,m,n,M,i,j):
        if i>=m or j>=n or i<0 or j<0:
            return 1
        
        if M<=0:
            return 0
        
        if memo[i][j][M] is not None:
            return memo[i][j][M]

        res=0
        res+=self.memoSol(memo,m,n,M-1,i+1,j)
        res+=self.memoSol(memo,m,n,M-1,i,j-1)
        res+=self.memoSol(memo,m,n,M-1,i-1,j)
        res+=self.memoSol(memo,m,n,M-1,i,j+1)
        memo[i][j][M]=res

        return res

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        return self.memoSol(memo,m,n,maxMove,startRow,startColumn) % (10**9 + 7)
