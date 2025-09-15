from fetch_helpers.fetch_team_games import fetch_team_games
from fetch_helpers.fetch_ap_teams import get_ap_teams


def score_ranked_wins(games, team_name, ranked_schools):
    ranked_win_count = 0
    for game in games:
        try:
            home = game["homeTeam"] 
            away = game["awayTeam"]
            home_pts = game["homePoints"]
            away_pts = game["awayPoints"]
            if home_pts is None or away_pts is None:
                continue          #Skips incomplete games
       
            team_is_home = home == team_name
            team_score = home_pts if team_is_home else away_pts
            opp_score = away_pts if team_is_home else home_pts
            opponent = away if team_is_home else home

            if team_score > opp_score and opponent in ranked_schools:
                ranked_win_count += 1
        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue
    return ranked_win_count
           


def score_regular_wins(games, team_name):
    win_count = 0

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
            
            if team_score > opp_score:
                win_count += 1

        except KeyError as e:
            print(f"Skipping game due to missing key: {e}")
            continue
    return win_count

