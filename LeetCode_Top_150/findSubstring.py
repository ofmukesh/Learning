def check_permutation (s,words,l_of_word):
    i=0
    tmp=[w for w in words]
    while i<len(s):
        if s[i:i+l_of_word] in tmp:
            tmp.remove(s[i:i+l_of_word])
        i+=l_of_word
    return True if not tmp else False

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans=[]

        l_of_word=len(words[0])
        l=len(words)*len(words[0])-1
        strt=0
        end=l

        while end<len(s):
            curr_s=s[strt:end+1]
            if check_permutation(curr_s,words,l_of_word):
                ans.append(strt)
            strt+=1
            end+=1

        return ans
