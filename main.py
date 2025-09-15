from fetch_helpers.fetch_all_teams import fetch_all_teams
from fetch_helpers.fetch_team_games import fetch_team_games
from score_helpers.calculate_team_record import calculate_team_record
from pprint import PrettyPrinter
from request_helper import get_json
from fetch_helpers.fetch_ap_teams import get_ap_teams
from score_helpers.score_ranked_wins import score_ranked_wins
from fetch_helpers.fetch_all_games import fetch_all_games
printer = PrettyPrinter(depth=4, width=120)
"""
Main entry point for generating team records and sorting Top 25 by win count.
"""

def main():
    all_teams = fetch_all_teams()
    all_games = fetch_all_games(2025)
    ranked_schools = {team["school"] for team in get_ap_teams(2025)}
    printer = PrettyPrinter(depth=5, width=120)
    records = []
    for team in all_teams:
        name = team["school"]
        team_games = [g for g in all_games if g["homeTeam"] == name or g["awayTeam"]== name]
        record = calculate_team_record(team_games, name)
        ranked_score = score_ranked_wins(team_games, name, ranked_schools)
        record["ranked_wins"] = ranked_score
        records.append(record)
    sorted_records = sorted(records, key=lambda x: x["ranked_wins"], reverse=True)
    for team in sorted_records[:25]:
        printer.pprint(f"{team['school']}: {team['wins']} wins, {team['ranked_wins']} ranked_wins")
    
  


if __name__ == "__main__":
    main()