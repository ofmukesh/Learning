def nStarTriangle(n: int) -> None:
    m=(n*2)-1
    mid=m//2
    for i in range(n):
        for j in range(m):
            if i<=j and m-i>j:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    pass
