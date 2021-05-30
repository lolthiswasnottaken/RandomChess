#!/usr/bin/env python3

#tests.py


import chess
import chess.svg
from IPython.display import SVG
import random
import time


class Game():
    def __init__(self):
        self.create_board()
        #self.display_board()
        self.legal_moves()

        self.make_first_move()
        self.display_board()

    def create_board(self):
        self.board = chess.Board()
    
    def display_board(self):
        print(self.board)

    def legal_moves(self):
        self.legal_moves = [str(i) for i in (self.board.legal_moves)]
    
    def decide_move(self):
        return random.randint(0,len(self.legal_moves)-1)

    def make_first_move(self):
        print(self.legal_moves[self.decide_move()])
        self.board.push_san(self.legal_moves[self.decide_move()])
        


g = Game()