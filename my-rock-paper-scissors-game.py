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