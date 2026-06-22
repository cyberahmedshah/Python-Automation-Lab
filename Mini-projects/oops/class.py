class student:
    
    def __init__(self, name, rollno, marks):
      self.name=name 
      self.rollno=rollno
      self.marks=marks

    def info(self):
     print(f"{self.name} is Roll No:{self.rollno} and got {self.marks} marks")

s1=student("Ahmed", "43", 91)

s2=student("Musa", "23", 31)

s3=student("Haleema", "02", 53)


result=input("Enter the rollno: ")

if result=="43":
   s1.info()
elif result=="23":
   s2.info()
elif result=="02":
   s3.info()
else:
   print("Roll no not found")
     
    