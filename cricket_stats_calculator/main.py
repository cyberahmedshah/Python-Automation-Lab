#importing the functions from the Batting module
from Batting import Batting_Average
from Batting import Batting_Strike_rate

# importing the functions from the Bowling module
from Bowling import Bowling_Average
from Bowling import Bowling_Strike_Rate

#A menu for the user to choose the type of stats they want calculate
print("Choose the type of stats you want to calculate:")
print("1. Batting Average")
print("2. Batting Strike Rate")
print("3. Bowling Average")
print("4. Bowling Strike Rate")

choice = int(input("Enter your choice (1 to 4): "))

if choice == 1:
    total_runs=int(input("Enter total runs scored: "))
    total_innings=int(input("Enter total innings played: "))
    not_outs=int(input(f"Enter total not outs: "))
    print(f"The batting average of batsman is: {Batting_Average(total_runs, total_innings, not_outs):.2f}")
elif choice == 2:
 total_runs=int(input("Enter total runs scored: "))
 total_balls=int(input("Enter total balls faced: "))
 print(f"The batting strike rate of batsman is: {Batting_Strike_rate(total_runs, total_balls):.2f}")
elif choice == 3:
    total_runs_conceded=int(input("Enter total runs conceded: "))
    total_wickets_taken=int(input("Enter total wickets taken: "))
    print(f"The bowling average of bowler is: {Bowling_Average(total_runs_conceded, total_wickets_taken):.2f}")
elif choice == 4:
    total_balls_bowled=int(input("Enter total balls bowled: "))
    total_wickets_taken=int(input("Enter total wickets taken: "))
    print(f"The bowling strike rate of bowler is: {Bowling_Strike_Rate(total_balls_bowled, total_wickets_taken):.2f}")
else:    print("Invalid choice. Please choose 1, 2, 3 or 4.")