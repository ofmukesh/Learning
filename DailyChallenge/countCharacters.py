class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsFreq={}
        for char in chars:
            charsFreq[char]=1+charsFreq.get(char,0)
        
        ans=0
        for word in words:
            tmp={}
            for char in word:
                tmp[char]=1+tmp.get(char,0)
            res=True
            for key in tmp.keys():
                if charsFreq.get(key,None) and tmp[key]<=charsFreq[key]:
                    res=True
                else:
                    res=False
                    break
            if res:
                ans+=len(word)
        return ans
