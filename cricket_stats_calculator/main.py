#importing the functions from the Batting module
from Batting import Batting_Average
from Batting import Batting_Strike_rate

# importing the functions from the Bowling module
from Bowling import Bowling_Average
from Bowling import Bowling_Strike_Rate

# importing the function from the NRR module
from NRR import net_run_rate

#A menu for the user to choose the type of stats they want calculate
print("Choose the type of stats you want to calculate:")
print("1. Batting Average")
print("2. Batting Strike Rate")
print("3. Bowling Average")
print("4. Bowling Strike Rate")
print("5. Net Run Rate")

choice = int(input("Enter your choice (1 to 5): "))

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
elif choice == 5:
    runs_scored=int(input("Enter total runs scored: "))
    overs_faced=int(input("Enter total overs faced(if the team was allout than enter the maximum number of overs): "))
    runs_conceded=int(input("Enter total runs conceded: "))
    overs_bowled=int(input("Enter total overs bowled(if the team was allout than enter the maximum number of overs): "))
    print(f"The net run rate of the team is: {net_run_rate(overs_faced, runs_scored, overs_bowled, runs_conceded):.2f}")
else:
    print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")