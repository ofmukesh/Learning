def nStarTriangle(n: int) -> None:
    m=n
    n=(n*2)-1
    for i in range((n//2)+1):
        for j in range(0,i):
            print("*",end="")
        print()

    for i in range((n//2)+1):
        for j in range(0,m-i):
            print("*",end="")
        print()
    pass
