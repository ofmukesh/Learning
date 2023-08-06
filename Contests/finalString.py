def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  

class Solution:
    def finalString(self, s: str) -> str:
        ans=""
        
        for w in s:
            if w=="i":
                ans=reverse_string(ans)
            else:
                ans+=w
        
        return ans
