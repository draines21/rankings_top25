from request_helper import get_json
from config import BASE_URL, CFBD_API_KEY



def fetch_all_games(year):
    url = f"{BASE_URL}/games"
    params = {"year": year,
              "seasonType": "regular"}
    return get_json(url, params=params)