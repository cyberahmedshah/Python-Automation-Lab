import random
secret_number=random.randint(1, 101)
for i in range(1, 6):
 guess=int(input(f"Attempt {i}, Guess the number(1-100): "))
 if guess==secret_number:
  print("Right! you won")
  break
 elif guess<secret_number:
  print ("Too low")
 else:
   print("Too high")
else:
 print("Game over, The secret number was:", secret_number)