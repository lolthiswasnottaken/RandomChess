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
        self.display_board()
    
    def create_board(self):
        self.board = chess.Board()
    
    def display_board(self):
        print(self.board)

g = Game()