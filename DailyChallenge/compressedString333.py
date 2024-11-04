class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        lastC=word[0]
        l=1

        for c in word[1:]:
            if c==lastC and l!=9:
                l+=1
            else:
                comp+=str(l)+lastC
                lastC=c
                l=1

        comp+=str(l)+lastC

        return comp
