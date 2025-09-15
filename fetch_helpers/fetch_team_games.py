import requests
from config import BASE_URL
from request_helper import get_json



def fetch_team_games(team, year):
    url = f"{BASE_URL}/games/teams"
    params = {
        "year": year,
        "team": team,
        "seasonType": "regular",
        "classification": "fbs"
    }

    return get_json(url, params)


