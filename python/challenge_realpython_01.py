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