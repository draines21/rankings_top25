from fetch_helpers.fetch_team_games import fetch_team_games
from fetch_helpers.fetch_ap_teams import get_ap_teams
from resume_weights import RESUME_WEIGHTS, POWER_CONFERENCES
weights = RESUME_WEIGHTS
power_confs = POWER_CONFERENCES
"""Calculates a score for wins against ranked and unranked opponents with a bonus based how high the opponent was ranked like Top 5 for example.
Also adds bonus for the conference opponent was in."""



def score_wins(games, team_name, ranked_schools, team_conferences):
    score = 0
    win_weight = weights["wins"]
    ranked_win_weight = weights["ranked_wins"]
    conf_bonus = weights["conference_bonus"]

    for game in games:
        try:
            home = game["homeTeam"]
            away = game["awayTeam"]
            home_pts = game["homePoints"]
            away_pts = game["awayPoints"]

            if home_pts is None or away_pts is None:
                continue  # skip future games

            team_is_home = home == team_name
            team_score = home_pts if team_is_home else away_pts
            opp_score = away_pts if team_is_home else home_pts
            opponent = away if team_is_home else home

            if team_score > opp_score:
                if opponent in ranked_schools:
                    rank = ranked_schools[opponent]
                    if rank <= 5:
                        multiplier = 2.0
                    elif rank <= 10:
                        multiplier = 1.5
                    else:
                        multiplier = 1.0
                    score += ranked_win_weight * multiplier
                else:
                    score += win_weight

                conf = team_conferences.get(opponent)
                if conf in power_confs:
                    score += conf_bonus * power_confs[conf]

        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue

    return score