from request_helper import get_json
from fetch_helpers.fetch_team_games import fetch_team_games


def calculate_team_record(team_games, team_name):
    wins = 0
    losses = 0

    for game in team_games:
        home = game.get("homeTeam")
        away = game.get("awayTeam")
        home_points = game.get("homePoints")
        away_points = game.get("awayPoints")

        # Skip bye games or future games
        if home_points is None or away_points is None:
            continue

        if team_name == home:
            if home_points > away_points:
                wins += 1
            elif home_points < away_points:
                losses += 1
        elif team_name == away:
            if away_points > home_points:
                wins += 1
            elif away_points < home_points:
                losses += 1

    return {"team": team_name, "wins": wins, "losses": losses}



 
