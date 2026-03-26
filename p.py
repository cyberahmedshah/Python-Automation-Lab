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


for i in range(11):
  
 if i==5:
        continue
 print(i)   
else:
    print("Loop tested")