## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n=int(input())

evSum=0
oddSum=0
while n!=0:

    if (n%10)%2==0:
        evSum+=(n%10)
    else:
        oddSum+=(n%10)
    n=n//10

print(evSum,oddSum)
