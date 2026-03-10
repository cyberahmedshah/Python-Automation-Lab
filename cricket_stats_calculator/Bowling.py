def Bowling_Average(total_runs_conceded, total_wickets_taken):
    if total_wickets_taken == 0:
        # No average if no wickets taken
        return float('0')
    else:  
     return total_runs_conceded / total_wickets_taken
    
def Bowling_Strike_Rate(total_balls_bowled, total_wickets_taken):
    if total_wickets_taken == 0:
        # No strike rate if no wickets taken
        return float('0')
    else:
     return total_balls_bowled / total_wickets_taken