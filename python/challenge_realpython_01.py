'''
There are two players.
Each player writes a number, hidden from the other player. It can be any integer 
1 or greater.
The players reveal their numbers.
Whoever chose the lower number gets 1 point, unless the lower number is lower 
by only 1, then the player with the higher number gets 2 points.
If they both chose the same number, neither player gets a point.
This repeats, and the game ends when one player has 5 points.
The challenge is to write a script to play this game. Knowing the rules and all 
your opponent’s previous numbers, can you program a strategy? 
(And, no - return random.randint(1, 3) is not a strategy.) You should really try 
playing this first with your friends - you’ll see there’s a deep human element 
to predicting your opponent’s choice.

Is it possible to program a strong strategy?

Want to make the strategy a bit more interesting? Add an additional constraint 
to the challenge so that players can only use each number once.
'''

class Player:
    def __init__(self, name) -> None:
        self.score = 0
        self.choices = []
        self.name = name

    def add_score(self, amount):
        self.score += amount
        print(f'Player {self.name} scored {amount} point(s) - Total: {self.score}')

    def add_choice(self, choice):
        self.choices.append(choice)

def check_choices(choice_1, choice_2, choices=[]):
    choices.append(choice_1)
    choices.append(choice_2)

    for choice in choices:
        pass

def main():
    print('running')
    player_1 = Player(name=input('Player 1, place your name: \n'))
    player_2 = Player(name=input('Player 2, place your name: \n'))
    round_count = 1

    while True:
        print(f'Round {round_count} started!')
        player_1_choice = input(f'{player_1}, choose a number: \n')
        player_2_choice = input(f'{player_2}, choose a number: \n')

        check_choices(player_1_choice, player_2_choice)


if __name__ == '__main__':
    main()