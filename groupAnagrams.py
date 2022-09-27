class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        while(len(strs)!=0):
            temp=[]
            ele=sorted(strs[len(strs)-1])
            j=len(strs)-1
            while(j>=0):
                if sorted(strs[j])==ele:
                    temp.append(strs[j])
                    strs.pop(j)
                j-=1
                    
            result.append(temp)
        return (result)
