class Team:
    def __init__(self, name):
        self.name = name
        self.runs_scored = 0
        self.overs_faced = 0
        self.runs_conceded = 0
        self.overs_bowled = 0

    def add_match_stats(self, runs_scored, overs_faced, runs_conceded, overs_bowled):
        self.runs_scored += runs_scored
        self.overs_faced += overs_faced
        self.runs_conceded += runs_conceded
        self.overs_bowled += overs_bowled

    def calculate_nrr(self):
        if self.overs_faced == 0 or self.overs_bowled == 0:
            return 0.0
        return (self.runs_scored / self.overs_faced) - (self.runs_conceded / self.overs_bowled)

def main():
    teams = []
    print("Cricket Tournament Net Run Rate Calculator")
    print("==========================================")

    num_teams = int(input("Enter the number of teams: "))

    for i in range(num_teams):
        team_name = input(f"Enter name for team {i+1}: ")
        teams.append(Team(team_name))

    num_matches = int(input("Enter the number of matches per team: "))

    for match in range(num_matches):
        print(f"\n--- Match {match+1} ---")
        for team in teams:
            print(f"\nEnter stats for {team.name}:")
            runs_scored = float(input("Runs scored: "))
            overs_faced = float(input("Overs faced: "))
            runs_conceded = float(input("Runs conceded: "))
            overs_bowled = float(input("Overs bowled: "))
            team.add_match_stats(runs_scored, overs_faced, runs_conceded, overs_bowled)

    # Calculate and display NRR
    print("\n\nTournament Standings by Net Run Rate:")
    print("=====================================")
    team_nrr = [(team.name, team.calculate_nrr()) for team in teams]
    team_nrr.sort(key=lambda x: x[1], reverse=True)

    for rank, (name, nrr) in enumerate(team_nrr, 1):
        print(f"{rank}. {name}: {nrr:.3f}")

if __name__ == "__main__":
    main()