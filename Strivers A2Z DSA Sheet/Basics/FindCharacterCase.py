## Read input as specified in the question.
## Print output as specified in the question.
s=input()

# if the character is an uppercase alphabet (A - Z).
if 65<=ord(s)<=90:
    print(1)
# if the character is a lowercase alphabet (a - z).
elif 97<=ord(s)<=122:
    print(0)
else:
    print(-1) #if the character is not an alphabet.
