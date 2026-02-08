# File for Minimax AI Algo
from copy import deepcopy
import pygame
import math # for INF

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf') # Edit: import math pkg for -INF
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, alpha, beta, False, game)[0] # edit: Max Player = FALSE
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break   # Beta Cutoff

        return maxEval, best_move

    else:
        minEval = float('inf') # Edit: import math pkg for INF
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, alpha, beta, True, game)[0] # Edit: Min Player = TRUE
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
            beta = min(beta, minEval)
            if beta <= alpha:
                break   # Alpha Cutoff

        return minEval, best_move

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves