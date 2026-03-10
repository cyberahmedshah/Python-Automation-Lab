#importing the functions from the Batting module
from Batting import Batting_Average
from Batting import Batting_Strike_rate

#A menu for the user to choose the type of stats they want calculate
print("Choose the type of stats you want to calculate:")
print("1. Batting Average")
print("2. Batting Strike Rate")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    total_runs=int(input("Enter total runs scored: "))
    total_innings=int(input("Enter total innings played: "))
    not_outs=int(input(f"Enter total not outs: "))
    print(f"The batting average of batsman is: {Batting_Average(total_runs, total_innings, not_outs):.2f}")
elif choice == 2:
 total_runs=int(input("Enter total runs scored: "))
 total_balls=int(input("Enter total balls faced: "))
 print(f"The batting strike rate of batsman is: {Batting_Strike_rate(total_runs, total_balls):.2f}")
