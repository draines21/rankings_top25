from resume_weights import RESUME_WEIGHTS, POWER_CONFERENCES
weights = RESUME_WEIGHTS


"""Creating a score for regular loss and count for losses to unranked opponents to which apply weights to later"""

def score_ranked_loss(games, team_name, ranked_schools):
    score = 0
    penalty = weights["loss"]
   
    
    
    for game in games:
        try:
            home = game["homeTeam"]
            away = game["awayTeam"]
            home_pts = game["homePoints"]
            away_pts = game["awayPoints"]

            if home_pts is None or away_pts is None:
                continue
            
            team_is_home = home == team_name
            team_score = home_pts if team_is_home else away_pts
            opp_score = away_pts if team_is_home else home_pts
            opponent = away if team_is_home else home
            if team_score < opp_score and opponent in ranked_schools:
                score += penalty   #negative value

        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue
    return score



def score_unranked_loss(games, team_name, ranked_schools):
    score = 0
    penalty = weights["unranked_loss"]


    for game in games:
        try:
            home = game["homeTeam"]
            away = game["awayTeam"]
            home_pts = game["homePoints"]
            away_pts = game["awayPoints"]

            if home_pts is None or away_pts is None:
                continue

            team_is_home = home == team_name
            team_score = home_pts if team_is_home else away_pts
            opp_score = away_pts if team_is_home else home_pts
            opponent = away if team_is_home else home

            if team_score < opp_score and opponent not in ranked_schools:
                score += penalty #more severe penalty
        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue
        
    return score



