# def feb_no(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return feb_no(n-1)+feb_no(n-2)

# n=int(input("Enter the number: "))
# print(feb_no(n))


# s={5,10,15}
# e={10, 20, 30}
# # print(s.union(e))
# # print(e.union(s))
# # print(s.intersection(e))
# # print(type(s))

# print(s.issuperset(e))
# print(s.isdisjoint(e))

# d={
#     111: "Ahmed",
#     112: "Hamza",
#     113: "Ali",
#     114: "Hassan"
# }


# d.pop(114)
# print(d)


#print(d[int(input("Enter the id: "))])

# print(d.keys())
# print(d.values())


# for key in d.keys():
#     print(d[key])


# dic={
#     int(input("Enter the id: ")): input("Enter the name: "),

# }


# for i in range(11):
  
#  if i==5:
#         continue
#  print(i)   
# else:
#     print("Loop tested")


# x=int(input("Enter the number: "))
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")


# for i in range(1,11):
#     if i%2==0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")



# for i in range(11):
#     if i==7:
#      continue
#     print(i)
# else:
#     print("working")



# for i in range(1, 6):
#     print(f"iteration no {i} in for loop")
# else:
#     print("end of loop")
# print("out of loop")


# try:
#  a=int(input("Enter the number: "))
#  for i in range(1, 11):
#   print(f"{a} x {i} = {(a)*i}")
# except:
#   print("Invalid input")

# # print("program working")



# a=int(input("Enter the number: "))
# for i in range(1,11):
#     if type(a) is int:
#         print(f"{a} x {i} = {a*i}")
#     elif type(a) is str:
#         print ("invalid input")



# def test(a, n):
#     try:
#      return a*n
#     finally:
#         print("Done")



# a= int(input("Number one: "))
# b= int(input("Number two: "))
# print(test(a, b))



# a=input("Enter the number(1-9): " ).lower()

# if a=="quit":
#     print("Program Exited")
#     exit()
# b=int(a)
# if b<1 or b>9:
#     raise ValueError
# if b>=1 and b<=9:
#     print("Program Working")



# a=[{"Questions":"Who created linux?", "OPtions":"a.me" "b.he" "c.they d.us", "answers":"a"}]
# answer=str(input("Enter the option: ")).strip().lower()
# if answer== a[{"answers"[1]}]:
#     print("correct")
# else:
#     print("wrong")


list=[
   {
      "Ahmed":["1", "2", "3"],
      "Amna":"2",
      "Khadija":"3"
      }
    ]
for i in list:
    print(i["Khadija"])
    for a in i["Ahmed"]:
     print(a)

