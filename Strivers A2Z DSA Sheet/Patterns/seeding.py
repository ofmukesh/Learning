def seeding(n: int) -> None:
    for i in range(n):
        for j in range(0,n-i):
            print("*",end=" ")
        print()
    pass
