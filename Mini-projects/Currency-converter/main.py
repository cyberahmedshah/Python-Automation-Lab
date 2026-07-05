print("Hey which currency you want to convert today \na.pesos \nb.soles \nc.reais \nd.All")
o=input("Enter the option(a,b,c and d: ").lower()
if o=="a":
  c=float(input("Enter the amount of co pesos you have: "))
  value=(c/17.44)
  print(f"You have ${value}")
elif o=="b":
  c=float(input("Enter the amount of pe soles you have: "))
  value=(c/3.14)
  print(f"You have ${value}")
elif o=="c":
  c=float(input("Enter the amount of Br reais you have: "))
  value=(c/5.18)
  print(f"You have ${value}")
elif o=="d":
  a=float(input("Enter the amount of pesos you have: "))
  b=float(input("Enter the amount of soles you have: "))
  c=float(input("Enter the amount of reais you have: "))
  p=a/17.44
  s=b/3.41
  r=c/5.18
  print(f"You have total ${p+s+r: .2f} left")
else:
  print("invalid option")

  

