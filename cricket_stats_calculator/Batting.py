def Batting_Average(total_runs, total_innings, not_outs):
    if total_innings - not_outs == 0:
        return 0
    else:
        return total_runs / (total_innings - not_outs)

def Batting_Strike_rate(total_runs, total_balls):
    if total_balls == 0:
        return 0
    else:
        return (total_runs / total_balls) * 100