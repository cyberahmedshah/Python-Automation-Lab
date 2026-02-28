o=(input("Enter the operation: "))
oprand=str(o)
x=int(input("Enter your first number: "))
y=int(input("Enter your second number: "))
z=int(input("Enter your third number: "))
w=int(input("Enter your fourth number: "))
if oprand== "+":
 print (x+y+z+w)
elif oprand== "-":
 print(x-y-z-w)
elif oprand== "*":
 print(x*y*z*w)
elif oprand== "/":
 print(x/y/z/w)
else:
 print("Invalid Operand")