class Solution:
    def printGfg(self, n,num=1):
        if num>n: return
        print("GFG",end=" ")
        self.printGfg(n,num+1)
