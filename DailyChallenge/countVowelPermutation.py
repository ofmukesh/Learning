class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # Initialize counts for each vowel
        countOfA = 1
        countOfE = 1
        countOfI = 1
        countOfO = 1
        countOfU = 1

        # Iterate from length 1 to n - 1
        for length in range(1, n):
            # Calculate counts for each vowel for the next length

            # 'a' can be followed by 'e'
            nextCountOfA = countOfE
            # 'e' can be followed by 'a' or 'i'
            nextCountOfE = (countOfA + countOfI)
            # 'i' can be followed by 'a', 'e', 'o', or 'u'
            nextCountOfI = (countOfA + countOfE + countOfO + countOfU)
            # 'o' can be followed by 'i' or 'u'
            nextCountOfO = (countOfI + countOfU)
            # 'u' can be followed by 'a'
            nextCountOfU = countOfA

            # Update the counts for each vowel for the next iteration
            countOfA = nextCountOfA
            countOfE = nextCountOfE
            countOfI = nextCountOfI
            countOfO = nextCountOfO
            countOfU = nextCountOfU

        # Calculate the total count and take modulo 1000000007 to prevent overflow
        totalCount = (countOfA + countOfE + countOfI + countOfO + countOfU) % 1000000007

        # Return the total count as an integer
        return int(totalCount)

'''
    n=1
     |-> strings we can make => a, e, i, o, u 
    n=2
     |- strings we can make
        a-> ae
        e-> ea,ei
        i-> ia, ie, io, iu
        o-> oi, ou, 
        u-> ua
    n=3
     |- strings we can make
        a-> aea, aei
        e-> eae,eia, eie, eio, eiu
        i...
    
    <--so the algo is works like this-->
    a is only followed by e and with e we can make ea, ei
    so a -> a + {strings we can make by e}
    a-> aea, aei
    '''

'''
Time complexity -> O(n)
Space complexity -> O(1)
'''
