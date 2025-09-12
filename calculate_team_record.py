from request_helper import get_json
from fetch_team_games import fetch_team_games


def calculate_team_record(team_games, team_name):
    wins = 0
    losses = 0

    for game in team_games:
        teams = game.get("teams", [])
        team_info = next((t for t in teams if t['team'] == team_name), None)
        opponent_info = next((t for t in teams if t["team"] != team_name), None)

        if team_info and opponent_info:
            if int(team_info["points"]) > int(opponent_info["points"]):
                wins += 1
            elif int(team_info["points"]) < int(opponent_info["points"]):
                losses += 1
    return {"team": team_name, "wins": wins, "losses": losses}



 
