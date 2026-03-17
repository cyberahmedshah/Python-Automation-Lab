a = input("Enter your inter percentage (e.g. 77%): ")

if a.endswith("%"):
    a = a[:-1]

percentage = float(a)

if percentage >= 90:
    print("You are eligible for 100% scholarship")
elif percentage >= 80:
    print("You are eligible for 75% scholarship")
elif percentage >= 70:
    print("You are eligible for 50% scholarship")
elif percentage >= 60:
    print("You are eligible for 25% scholarship")
else:
    print("You are not eligible for scholarship")