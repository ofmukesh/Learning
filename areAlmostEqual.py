class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        temp=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if len(temp)==2:
                    return False;
                else:
                    temp.append(i);
        if len(temp)==0:
            return True
        elif len(temp)==1:
            return False
        elif s1[temp[0]]!=s2[temp[1]] or s1[temp[1]]!=s2[temp[0]]:
                return False
        else:
            return True     
