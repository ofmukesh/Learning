class Solution:    
    #Complete this function
    def rec(self,num,N):
        if num>N: return
        print(num,end=" ")
        self.rec(num+1,N)
        
    def printNos(self,N):
        self.rec(1,N)
