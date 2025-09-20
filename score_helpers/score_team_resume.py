from fetch_helpers.fetch_all_teams import fetch_all_teams
from fetch_helpers.fetch_all_games import fetch_all_games
from fetch_helpers.fetch_ap_teams import get_ap_teams
from score_helpers.calculate_team_record import calculate_team_record
from score_helpers.score_ranked_wins import score_ranked_wins, score_regular_wins
from score_helpers.score_losses import score_ranked_loss, score_unranked_loss
from score_helpers.score_margin import score_margin_of_victory
from resume_weights import RESUME_WEIGHTS
from pprint import PrettyPrinter
printer = PrettyPrinter(depth=4, width=120)

"""Calculates a team resume score based off things such as ranked wins and losses as well as margin of victory"""



def score_team_resume(games, team_name, ranked_schools, weights, team_conferences):
    record = calculate_team_record(games, team_name)
    score_for_ranked_wins = score_ranked_wins(games, team_name, ranked_schools, team_conferences)
    score_for_regular_wins = score_regular_wins(games, team_name, team_conferences)
    score_for_ranked_loss = score_ranked_loss(games, team_name, ranked_schools)
    score_for_unranked_loss = score_unranked_loss(games, team_name, ranked_schools)
    margin_victory_score = score_margin_of_victory(games, team_name, ranked_schools, weights)


    resume_score = 0

    resume_score += score_for_ranked_wins
    resume_score += score_for_regular_wins
    resume_score += score_for_ranked_loss
    resume_score += score_for_unranked_loss
    resume_score += margin_victory_score
    return resume_score, record







