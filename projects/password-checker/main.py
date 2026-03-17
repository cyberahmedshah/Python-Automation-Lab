correct_password="Binarytrade123"
for i in range(1, 4):
    key=(str(input(f"Attempt {i}: Enter the password: ")))
    if key==correct_password:
     print("Access granted")
     break
    elif i<3:
       print("Wrong password! Try again")
else:
       print("Account Locked")