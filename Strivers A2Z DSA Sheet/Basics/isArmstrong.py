def isArmstrong(N):
    n=0
    dup=N
    while N!=0:
        n+=(N%10)**3
        N//=10
    if dup==n:
        return True
    else:
        return False

q=[153,371,35,1]
for num in q:
    res=isArmstrong(num)
    
    if res:
        print(f"{num} is a armstrong number")
    else:
        print(f"{num} is not a armstrong number")
