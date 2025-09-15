from fetch_helpers.fetch_ap_teams import get_ap_teams


"""Creating a loss count for regular loss and count for losses to unranked opponents to which apply weights to later"""

def score_loss(games, team_name, ranked_schools):
    loss_count = 0
    
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
                loss_count += 1

        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue
    return loss_count



def score_bad_loss(games, team_name, ranked_schools):
    loss_count = 0

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
                loss_count += 1
        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue
        
    return loss_count



