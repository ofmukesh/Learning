# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         a=""
#         b=""
        
#         i=0
#         l=len(s)-1
#         while i<=l:
#             if s[i].isalnum():
#                 a+=s[i].lower()
#             if s[l-i].isalnum():
#                 b+=s[l-i].lower()
#             i+=1

#         if a==b:
#             return True
#         return False



# optimized using two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<=r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False

        return True
                
