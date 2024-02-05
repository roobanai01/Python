a=input("Enter the Value:")
b=input("Choose square or cube:")
b=(b.lower())
if "square" in b:
    c=int(a)*int(a);
    print("The square Value of "+ a +" is:",c)
elif "cube" in b:
    c=int(a)*int(a)*int(a);
    print("The cube Value of "+ a +" is:",c)
else:
    print("Please choose the correct option.")