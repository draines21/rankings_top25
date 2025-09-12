from fetch_team_games import fetch_team_games
from pprint import PrettyPrinter
from calculate_team_record import calculate_team_record


printer = PrettyPrinter(depth=4, width=120)
games = fetch_team_games("Oregon", 2025)
record = calculate_team_record(games, "Oregon")
printer.pprint(record)