class Solution:
    def totalNQueens(self, n: int) -> int:
        def search(queens, dif, sum):
            l = len(queens)
            if l == n:
                self.ans += 1
                return None
            for q in range(n):
                if q not in queens and l-q not in dif and l+q not in sum:
                    search(queens+[q], dif+[l-q], sum+[l+q])
        
        self.ans = 0
        search([],[],[])
        return self.ans
