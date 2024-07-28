# Merges two strings by alternating characters from each string (using turning method). Handles remaining characters if strings have different lengths.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        turn1=True
        i=0
        merged=""
        while i<len(word1) and i<len(word2):
            if turn1:
                merged+=word1[i]
                turn1=False
            else:
                merged+=word2[i]
                turn1=True
                i+=1

        if i>=len(word1):
            merged+=word2[i:]
        else:
            merged+=word1[i:]
        
        return merged
