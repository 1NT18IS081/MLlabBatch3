a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = input("Enter the operator : ")
if(c == '+'):
    d = int(a + b)
    print("The value of a + b is")
    print(d)
elif(c == '-'):
    d = int(a - b)
    print("The value of a - b is")
    print(d)
elif(c == '/'):
    d = int(a / b)
    print("The value of a / b is")
    print(d)
else:
    d = int(a * b)
    print("The value of a * b is")
    print(d)              
Enter the value of a : 10
Enter the value of b : 10
Enter the operator : *
The value of a *b is
100
