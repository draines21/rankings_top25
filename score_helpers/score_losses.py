from resume_weights import RESUME_WEIGHTS, POWER_CONFERENCES
weights = RESUME_WEIGHTS


"""Creating a score for regular loss and count for losses to unranked opponents to which apply weights to later"""

def score_losses(games, team_name, ranked_schools, weights):
    score = 0
    ranked_loss_penalty = weights["loss"]
    unranked_loss_penalty = weights["unranked_loss"]

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

            if team_score < opp_score:
                if opponent in ranked_schools:
                    score += ranked_loss_penalty   # "good" loss
                else:
                    score += unranked_loss_penalty # "bad" loss

        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue

    return score