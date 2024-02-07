r=int(input("Enter the value:"))
factorial =1
if r<0:
    print("Factorial does not exist")
elif r==0:
    print("factorial is 1 ")
else:
    for r in range(1,r+1):
        factorial = factorial * r
    print("factorial of ",r," is :",factorial)