def nStarDiamond(n: int) -> None:
    m=(n*2)-1
    midCol=m//2
    n=n*2
    midRow=n//2
    for i in range(n):
        for j in range(m):
            if i<=midRow:
                if midCol-i<=j<=midCol+i:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if i-midCol-1<=j<m-(i-midRow):
                    print("*",end="")
                else:
                    print(" ",end="")
        print()
