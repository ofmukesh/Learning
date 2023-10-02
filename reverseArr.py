arr=[1,2,3,4,5,6]
n=len(arr)-1
j=0
i=n
while n>=0:
    arr.insert(j,arr[i])
    arr.pop()
    j+=1
    n-=1
print(arr)
# T.C > O(n)
# S.c > O(1)
