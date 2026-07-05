def bmi():
  w=int(input("Enter Your Body weight(kg): "))
  h=int(input("Enter Your Height(Cm): "))
  hm=h/100
  h2=hm**2
  return w/h2

print(bmi())