oprand=0
while oprand != "quit":
 num1=float(input("Enter the number: "))
 oprand=input("Enter oprand(+,-,*,/): ")
 num2=float(input("Enter the number: "))

 if oprand=="+":
    print(num1+num2)
 elif oprand=="-":
    print(num1-num2)
 elif oprand=="*":
    print(num1*num2)
 elif oprand=="/":
    print(num1/num2)