RESUME_WEIGHTS = {"wins": 1.0,              # regular win
                  "ranked_wins": 2.0,       # win vs ranked opponent
                  "score_margin": 0.25,     # .25 for every 6pts in the margin
                  "loss": -1.0,             # loss to good team
                  "unranked_loss": -3.0,    # loss to bad team
                  "conference_bonus": 0.5}  # bonus for win against a team in stronger conference