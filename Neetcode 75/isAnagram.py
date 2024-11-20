class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for c in s:
            char_dict[c]+=1
        
        for c in t:
            char_dict[c]-=1
        
        for key in char_dict.keys():
            if char_dict[key]!=0:
                return False
        
        return True
