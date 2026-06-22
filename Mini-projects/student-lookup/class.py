class student:
    
    def __init__(self, name, rollno, marks):
      self.name=name 
      self.rollno=rollno
      self.marks=marks

    def info(self):
     print(f"{self.name} is Roll No:{self.rollno} and got {self.marks} marks")

students=[


student("Ahmed", "43", 91),

student("Musa", "23", 31),

student("Haleema", "02", 53)
]


result=input("Enter the rollno: ")

for i in students:
   if result==i.rollno:
      i.info()
   else:
    print("Roll no not found")
     
    