import random

pose = [1, 2, 3]
labels = {1: 'rock', 2: 'paper', 3: 'scissor'}

print("Choose the option by entering the number")
print("1. Rock\n2. Paper\n3. Scissor")

while True:
    user = input("Enter any pose (1/2/3 or q to quit): ").lower()

    if user == "q":
        print("Game exited")
        break

    if not user.isdigit() or int(user) not in pose:
        print("Enter valid pose")
        continue

    user_choice = int(user)
    computer = random.choice(pose)

    print(f"You chose {labels[user_choice]}, computer chose {labels[computer]}.")

    if user_choice == computer:
        print("It's a Draw")
    elif user_choice == 1 and computer == 2:
        print("Ohh! You Lost")
    elif user_choice == 1 and computer == 3:
        print("You Won!")
    elif user_choice == 2 and computer == 1:
        print("You Won!")
    elif user_choice == 2 and computer == 3:
        print("Ohh! You Lost")
    elif user_choice == 3 and computer == 1:
        print("Ohh! You Lost")
    elif user_choice == 3 and computer == 2:
        print("You Won!")

