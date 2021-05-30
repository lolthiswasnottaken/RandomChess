#!/usr/bin/env python3

#main.py

import chess
import chess.svg
from IPython.display import SVG
import random
import time


class Game():
    def __init__(self):
        self.create_board()

        self.make_n_random_moves(2)

        
        self.display_board()

        self.import_fen("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
        self.display_board()
    

    def create_board(self):                 #creates board with initial state
        self.board = chess.Board()
    
    def display_board(self):                #displays boards in console ref: https://python-chess.readthedocs.io/en/latest/
        print(self.board)

    def legal_moves(self):                  #self.legal_moves as a list
        self.legal_moves_list = [str(i) for i in (self.board.legal_moves)]
    
    def decide_move(self):                  #decides what move to make randomly
        self.legal_moves()
        return random.randint(0,len(self.legal_moves_list)-1)

    def make_move(self):                    #makes one move randomly
        self.legal_moves()
        self.board.push_san(self.legal_moves_list[self.decide_move()])

    def make_n_random_moves(self,n):        #makes n random moves for total of both sides
        for i in range(n):
            self.make_move()
            if self.board.is_game_over():
                print("Game ended")
                break
        
    def import_fen(self,fen):

        self.board.clear()
        self.board.set_fen(fen)      


g = Game()