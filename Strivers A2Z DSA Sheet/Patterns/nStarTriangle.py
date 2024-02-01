def nStarTriangle(n: int) -> None:
    m=n*2
    mid=(m//2)-1
    for i in range(n):
        for j in range(m):
            if mid-i<=j and j<=mid+i:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    pass
