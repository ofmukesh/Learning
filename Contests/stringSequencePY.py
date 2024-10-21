'''
Append the current string while the current character is not same as the current target character,
and if the target char.. is matched with curr char.. then just add "a" at the end of the current string,
and please don't forget to append the current string to the answer array.
'''
class Solution:
    dump={'a': 'b','b': 'c','c': 'd','d': 'e','e': 'f','f': 'g','g': 'h','h': 'i','i': 'j','j': 'k','k': 'l','l': 'm','m': 'n','n': 'o','o': 'p','p': 'q','q': 'r','r': 's','s': 't','t': 'u','u': 'v','v': 'w','w': 'x','x': 'y','y': 'z','z': "a"}

    def stringSequence(self, target: str) -> List[str]:
        currS="a"
        currC="a"
        ans=["a"]
        targetIdx=0
        target=list(target)
        
        while targetIdx<len(target):
            if currC==target[targetIdx]:
                currS+="a"
                currC="a"
                targetIdx+=1
                if targetIdx<len(target):
                    ans.append(currS)
            else:
                currS=currS[:len(currS)-1]+self.dump[currC]
                currC=self.dump[currC]
                ans.append(currS)
        
        return ans
