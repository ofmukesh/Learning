def nBinaryTriangle(n: int) -> None:
    f=1
    for i in range(n):
        t=f
        for j in range(0,i+1):
            print(t, end=" ")
            t=1 if t==0 else 0
        print()
        f=1 if f==0 else 0
    pass
