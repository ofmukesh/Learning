class Solution:
    def result(self,arr):
        occ={}
        idx=0
        res=[None for _ in arr]
        for i,val in enumerate(arr):
            if occ.get(val)!=None:
                res[i]=occ[val]
            else:
                res[i]=idx
                occ[val]=idx
                idx+=1
        
        return res
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr1=self.result(s)
        arr2=self.result(t)
        
        return arr1==arr2
