# def feb_no(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return feb_no(n-1)+feb_no(n-2)

# n=int(input("Enter the number: "))
# print(feb_no(n))


s={5,10,15}
e={10, 20, 30}
print(s.union(e))
print(e.union(s))
print(s.intersection(e))
print(type(s))