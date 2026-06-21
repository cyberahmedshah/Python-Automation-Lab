class student:
     name="Ahmed"
     rollno="43"
     marks=91
     def info(self):
      print(f"{self.name} is Roll no:{self.rollno} and got {self.marks} marks")

s1=student()

s2=student()
s2.name="Musa"
s2.rollno="23"
s2.marks=31

s3=student()
s3.name="Haleema"
s3.rollno="02"
s3.marks=65


result=input("Enter the rollno: ")

if result=="43":
   s1.info()
elif result=="23":
   s2.info()
elif result=="02":
   s3.info()
else:
   print("Roll no not found")
     
    