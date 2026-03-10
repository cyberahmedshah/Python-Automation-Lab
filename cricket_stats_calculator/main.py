from Batting import Batting_Average
from Batting import Batting_Strike_rate
total_runs=int(input("Enter total runs scored: "))
total_innings=int(input("Enter total innings played: "))
not_outs=int(input(f"Enter total not outs: "))
total_balls=int(input("Enter total balls faced: "))
print(f"The batting average of batsman is: {Batting_Average(total_runs, total_innings, not_outs)}")
print(f"The batting strike rate of batsman is: {Batting_Strike_rate(total_runs, total_balls)}")