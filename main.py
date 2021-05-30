#!/usr/bin/env python3

#main.py
import chess
import chess.svg
from IPython.display import SVG
import random
import time

board = chess.Board()
game_pgn = []
#legal_moves = [str(i) for i in list(board.legal_moves)]
legal_moves= [1]
moves = 1
game_num= 0
while 1:
  
        
        legal_moves = [str(i) for i in list(board.legal_moves)]
        move_ind = random.randint(0,len(legal_moves)-1)
        board.push_san(legal_moves[move_ind])
        game_pgn.append("{}.{}".format(int(moves),legal_moves[move_ind]))
        
        #time.sleep(1)


        #print(board.board_fen)
        #print(game_pgn)
        print(board,"\n")
        #print(board.fen)
        moves += 0.5
    
                
        if board.is_game_over():

            if board.is_checkmate():
                pass
                #boardsvg = chess.svg.board(board=board)
                #outputfile = open('board_images/game#{}.svg'.format(game_num), "w")
                #outputfile.write(boardsvg)
                #outputfile.close()

            board.clear
            board = chess.Board()
            game_pgn = []
            moves = 1
            game_num += 1   
                
    
