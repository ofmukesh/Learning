class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","").lower()

        if s=="": return True

        mid=len(s)//2
        i=0
        j=len(s)-1
        while i<=mid:
            if not s[i].isalnum(): i+=1
            elif not s[j].isalnum(): j-=1
            else:
                # if the string is not a Valid Palindrome
                if s[i]!=s[j]:
                    return False
                    
                i+=1
                j-=1

        return True
