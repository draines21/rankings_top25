from fetch_helpers.fetch_all_teams import fetch_all_teams
from fetch_helpers.fetch_all_games import fetch_all_games
from fetch_helpers.fetch_ap_teams import get_ap_teams
from score_helpers.calculate_team_record import calculate_team_record
from score_helpers.score_ranked_wins import score_ranked_wins
from resume_weights import RESUME_WEIGHTS

"""Calculates a team resume score based off things such as ranked wins and losses as well as margin of victory"""


def score_team_resume(games, team_name, ranked_schools):
    record = calculate_team_record(games, team_name)
    score_for_ranked_wins = score_ranked_wins(games, team_name, ranked_schools)

