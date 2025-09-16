from fetch_helpers.fetch_all_games import fetch_all_games
from fetch_helpers.fetch_ap_teams import get_ap_teams
from score_helpers.score_team_resume import score_team_resume, count_for_bad_loss, score_for_bad_loss
from resume_weights import RESUME_WEIGHTS

def test_team_resume(team_name):
    games = fetch_all_games(2025)
    ranked_schools = get_ap_teams(2025)
    team_games = [game for game in games if game["homeTeam"] == team_name or game["awayTeam"] == team_name]

    score, record = score_team_resume(team_games, team_name, ranked_schools, RESUME_WEIGHTS)
    print(f"{team_name} resume score: {score:.2f} | Record: {record['wins']}-{record['losses']}")
    print(f"Bad loss count: {count_for_bad_loss}")
    print(f"Penalty applied: {score_for_bad_loss}")



if __name__ == "__main__":
    test_team_resume("Florida")