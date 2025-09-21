RESUME_WEIGHTS = {"wins": 1.0,              # regular win
                  "ranked_wins": 5.0,       # win vs ranked opponent
                  "score_margin": 0.25,     # .25 for every 6pts in the margin
                  "loss": -1.0,             # loss to good team
                  "unranked_loss": -5.0,    # loss to bad team
                  "conference_bonus": 0.5 }  # bonus for win against a team in stronger conference


POWER_CONFERENCES = {'Big Ten': 1.4,
                     'SEC': 1.5,
                     'ACC': 1.2,
                     'Big 12': 1.2,
                     'Pac-12': 1.0}