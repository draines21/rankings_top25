from fetch_helpers.fetch_all_teams import fetch_all_teams
from pprint import PrettyPrinter
from fetch_helpers.fetch_ap_teams import get_ap_teams
from fetch_helpers.fetch_all_games import fetch_all_games
from score_helpers.score_team_resume import score_team_resume
from resume_weights import RESUME_WEIGHTS
printer = PrettyPrinter(depth=4, width=120)
"""
Main entry point for generating all the teams resume scores and sorting them into the Top 25 teams in the country.
"""

def main():
    all_teams = fetch_all_teams()
    all_games = fetch_all_games(2025)
    ranked_schools = {team["school"] for team in get_ap_teams(2025)}
    resume_ranks = []
    for team in all_teams:
        name = team["school"]
        team_games = [game for game in all_games if game["homeTeam"] == name or game["awayTeam"]== name]

        if not team_games:
            continue
        score, record = score_team_resume(team_games, name, ranked_schools, RESUME_WEIGHTS)
        resume_ranks.append({"team": name,
                             "score": score,
                             "record": record})
    top_25 = sorted(resume_ranks, key=lambda x: x["score"], reverse=True)[:25] 
    for rank, team in enumerate(top_25, start=1):
        printer.pprint(f"{rank}. {team['team']} ({team['record']['wins']}-{team['record']['losses']}) — Score: {team['score']:.2f}")


        
    
  


if __name__ == "__main__":
    main()