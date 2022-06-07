'''
Premier League Champions
Create a function that takes a list of football clubs with properties: name, 
wins, loss, draws, scored, conceded, and returns the team name with the highest 
number of points. If two teams have the same number of points, return the team 
with the largest goal difference.

How to Calculate Points and Goal Difference
team = { 
    "name": "Manchester United", 
    "wins": 30, 
    "loss": 3, 
    "draws": 5, 
    "scored": 88, 
    "conceded": 20 
    }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 
                                                                    95 points
Goal Difference = scored - conceded = 88 - 20 = 68
Examples
champions([
  {
    "name": "Manchester United",
    "wins": 30,
    "loss": 3,
    "draws": 5,
    "scored": 88,
    "conceded": 20,
  },
  {
    "name": "Arsenal",
    "wins": 24,
    "loss": 6,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  },
  {
    "name": "Chelsea",
    "wins": 22,
    "loss": 8,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  }
]) ➞ "Manchester United"
Notes
Input is a list of teams.
'''
clubs_list = [
  {
    "name": "Manchester United",
    "wins": 30,
    "loss": 3,
    "draws": 5,
    "scored": 88,
    "conceded": 20,
  },
  {
    "name": "Arsenal",
    "wins": 24,
    "loss": 6,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  },
  {
    "name": "Chelsea",
    "wins": 30,
    "loss": 3,
    "draws": 5,
    "scored": 108,
    "conceded": 29,
  }
]

def champions(clubs):
    param_total = 0
    bigger = {'total_points': 0}

    for club in clubs:
        club['total_points'] = 3 * club['wins'] + 0 * club['loss'] + 1 * club['draws']
        club['goal_difference'] = club['scored'] - club['conceded']
        print(f'{club["name"]} => {club["goal_difference"]}')

        if club['total_points'] == bigger['total_points']:
            if club['goal_difference'] > bigger['goal_difference']:
                return club['name']
            else:
                return bigger['name']

        if club['total_points'] > param_total:
            param_total = club['total_points']
            bigger = club
    
    return bigger['name']

        
# clubs2 = champions(clubs_list)
# print(clubs2)
print(champions(clubs_list))