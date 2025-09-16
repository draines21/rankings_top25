from fetch_helpers.fetch_all_games import fetch_all_games
from fetch_helpers.fetch_ap_teams import get_ap_teams
from score_helpers.score_margin import score_margin_of_victory
from resume_weights import RESUME_WEIGHTS

def test_margin(team_name):
    games = fetch_all_games(2025)
    ranked_schools = get_ap_teams(2025)
    team_games = [game for game in games if game["homeTeam"] == team_name or game["awayTeam"] == team_name]

    margin_score = score_margin_of_victory(team_games, team_name, ranked_schools, RESUME_WEIGHTS)
    print(f"{team_name} margin of victory score: {margin_score:.2f}")

if __name__ == "__main__":
    test_margin("Oregon")