def net_run_rate(overs_faced, runs_scored, overs_bowled, runs_conceded):
    if overs_faced == 0 or overs_bowled == 0:
        return 0.0
    else:
        nrr = (runs_scored / overs_faced) - (runs_conceded / overs_bowled)
        return nrr
    
def convert_overs(overs):
    overs = str(overs)
    if "." in overs:
        o, balls = overs.split(".")
        return int(o) + int(balls) / 6
    return float(overs)