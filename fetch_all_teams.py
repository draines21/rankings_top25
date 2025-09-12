import requests 
from config import BASE_URL
from request_helper import get_json


def fetch_all_teams():
    url = f"{BASE_URL}/teams/fbs"
    return get_json(url)
    