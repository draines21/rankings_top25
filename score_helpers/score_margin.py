from resume_weights import RESUME_WEIGHTS

"""calculates scoring margin and adds a bonus for per 6 pts of difference"""




def score_margin_of_victory(games, team_name, ranked_schools, weights):
    margin_score = 0
    margin_weight = weights["score_margin"]
    for game in games:
        home_pts = game["homePoints"]
        away_pts = game["awayPoints"]

        if home_pts is None or away_pts is None:
            continue

        home = game["homeTeam"]
        away = game["awayTeam"]
        team_is_home = home == team_name
        team_score = home_pts if team_is_home else away_pts
        opp_score = away_pts if team_is_home else home_pts
        opponent = away if team_is_home else home

        if team_score > opp_score:
            margin = team_score - opp_score
            units = min(margin // 6, 5)
            bonus = units * margin_weight
            if opponent in ranked_schools:
                rank = ranked_schools[opponent]
                if rank <= 5:
                    bonus *= 1.5
                elif rank <= 10:
                    bonus *+ 1.3
                else:
                    bonus *= 1.1
            margin_score += bonus




    return margin_score



        


