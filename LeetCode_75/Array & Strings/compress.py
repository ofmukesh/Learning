class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        while i<len(chars):
            curr=chars[i]
            count=1
            j=i+1
            while j<len(chars):
                if curr == chars[j]:
                    chars.pop(j)
                    count+=1
                else:
                    break
            if 10>count>1:
                chars.insert(i+1,str(count))
                i+=2
            elif count>9:
                counts=str(count)
                k=i+1
                for c in counts:
                    chars.insert(k,c)
                    k+=1
                    i+=1
            else:
                i+=1
        return len(chars)
