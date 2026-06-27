import random
pose=[
    "rock",
    "paper",
    "scissor"
]

computer=random.choice(pose)
user=input("Enter any pose(rock, paper, scissor ): ").lower()

while True:
 if user==computer:
     print("It's a Draw")
 elif user=="rock" and computer=="paper":
     print("Ohh! You Lost")
 elif user=="rock" and computer=="scissor":
     print("You Won!")
 elif user=="paper" and computer=="rock":
     print("You Won!")
 elif user=="paper" and computer=="scissor":
     print("Ohh! You Lost")
 elif user=="scissor" and computer=="rock":
     print("Ohh! You Lost")
 elif user=="scissor" and computer=="paper":
     print("You Won!")
 elif user==("q"):
     print("Game exited")
     break
 else:
     print("Enter valid pose")