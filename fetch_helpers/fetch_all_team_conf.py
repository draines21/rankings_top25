from fetch_helpers.fetch_all_teams import fetch_all_teams
from .cache_helpers import load_or_fetch
from config import BASE_URL

def conference_team_map():
    filename = "team_conferences_2025.json"
    teams = load_or_fetch(filename, lambda: fetch_all_teams())
    team_conferences = {}
    for team in teams:
        school = team.get("school")
        conference = team.get("conference")
        if school and conference:
            team_conferences[school] = conference
    return team_conferences




