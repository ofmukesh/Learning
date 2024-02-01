def nNumberTriangle(n: int) -> None:
    for i in range(n):
        for j in range(0,n-i):
            print(j+1,end=" ")
        print()
    pass
