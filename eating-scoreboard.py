"""
Question
You are the judge at a competitive eating competition and you need to choose a winner!

There are three foods at the competition and each type of food is worth a different amount of points. Points are as follows:

    Chickenwings: 5 points

    Hamburgers: 3 points

    Hotdogs: 2 points

Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the participants, for example:

[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]

It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.

[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]
"""

#SOLUTION
def calculate_score(participant):
    #total score for each participant based on the given points
    score = participant["chickenwings"] * 5 + participant["hamburgers"] * 3 + participant["hotdogs"] * 2
    return score

def scoreboard(who_ate_what):
    # scores for each participant
    scores = [{"name": participant["name"], "score": calculate_score(participant)} for participant in who_ate_what]

    # Sort scoreboard by score and then alphabetically by name
    sorted_scores = sorted(scores, key=lambda x: (-x["score"], x["name"]))

    return sorted_scores

# Example usage
participants = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

result = scoreboard(participants)
print(result)
