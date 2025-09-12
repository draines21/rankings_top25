from config import BASE_URL
from request_helper import get_json
from pprint import PrettyPrinter

printer = PrettyPrinter(depth=4, width=120)


def get_ap_teams(year):
    rankings = get_json(f"{BASE_URL}/rankings?year={year}&poll=AP Top 25")
    latest_week = max(entry["week"] for entry in rankings)
    latest_entry = next(entry for entry in rankings if entry["week"] == latest_week)
    ap_poll = next(poll for poll in latest_entry["polls"] if poll["poll"] == "AP Top 25")
    return ap_poll["ranks"]

printer.pprint(get_ap_teams(2025))

