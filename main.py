class student:
    def __init__(self, name, rollno, marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def result(self):
        print(f"{self.name} is Rollno. {self.rollno} and got {self.marks} Marks")



students=[
student("ahmed", "43", 91),
student("musa", "23", 31),
student("huhu", "02", 45)
]
r=input("Enter the roll no: ")

for i in students:
 if r==i.rollno:
    i.result()
 else:
    print("Nothing")
