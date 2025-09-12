from fetch_all_teams import fetch_all_teams
from fetch_team_games import fetch_team_games
from calculate_team_record import calculate_team_record
from pprint import PrettyPrinter
from request_helper import get_json




def main():
    teams = fetch_all_teams()
    printer = PrettyPrinter(depth=5, width=120)
    records = []
    for team in teams:
        name = team["school"]
        games = fetch_team_games(name, 2025)
        record = calculate_team_record(games, name)
        records.append(record)
    sorted_records = sorted(records, key=lambda x: x["wins"], reverse=True)
    
    printer.pprint(sorted_records)
    print("\nTop 25 by win count:")
    for team in sorted_records[:25]:
        print(team)


if __name__ == "__main__":
    main()