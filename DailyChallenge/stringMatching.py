class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        '''
        the isSubstring function is used to check a string 
        s1 is subsstring of string s2 or not 
        '''
        def isSubstring(s1,s2):
            if len(s1)>len(s2): return False # if s1 is bigger than s2, means possibly s1 is not a substring of s2

            if s1 in s2:
                return True
            
            return False
        
        # solution
        ans=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if isSubstring(words[i],words[j]):
                        ans.append(words[i])
                        break
        
        return ans
