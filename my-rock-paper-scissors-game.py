import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        self.my_next_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        response = valid_input("Please choose rock, paper, or scissors\n")
        return response


class ReflectPlayer(Player):
    def __init__(self):
        self.my_next_move = random.choice(moves)

    def move(self):
        if self.my_next_move == 'rock':
            return 'rock'
        elif self.my_next_move == 'paper':
            return 'paper'
        elif self.my_next_move == 'scissors':
            return 'scissors'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        self.my_next_move = their_move


def valid_input(prompt):
    response = input(prompt)
    while response not in moves:
        print("Invalid input, please choose again")
        return valid_input(prompt)
    return response


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class AllRockPlayer(Player):
    def move(self):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 played {move1}")
        print(f"Player 2 played {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("You have tied this round:")
            print(f"Player 1's score is {self.p1_score}")
            print(f"Player 2's score is {self.p2_score}")
        elif Game.beats(move1, move2):
            self.p1_score += 1
            print("Player 1 has won this round:")
            print(f"Player 1's score is {self.p1_score}")
            print(f"Player 2's score is {self.p2_score}")
        else:
            self.p2_score += 1
            print("Player 2 has won this round:")
            print(f"Player 1's score is {self.p1_score}")
            print(f"Player 2's score is {self.p2_score}")

    def play_game(self):
        print("The game has begun!")
        self.rounds = 3
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        print(f"Player 1's final score is {self.p1_score}!")
        print(f"Player 2's final score is {self.p2_score}!")
        print("Well done everyone, the game has ended!")


if __name__ == '__main__':
    game = Game(ReflectPlayer(), HumanPlayer())
    game.play_game()
