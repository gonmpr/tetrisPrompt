import sys, tty, termios, time
from tools import set_terminal, restart_terminal, draw, clear_terminal
from board import board_state # board[row][col]
from constants import SYMBOL, BOARD_WIDTH, BOARD_HEIGHT
import random

class Piece:
    def __init__(self, form):
        self.previous_position = form #[(a,b)(a,b)]
        self.next_position = [] #[(a,b)(a,b)]
        self.can_move_down = True
        self.can_move_sideways = True


    def move_sideways(self, char):
        self.next_position = []
        self.can_move_sideways = True


        for row, col in self.previous_position:
            new_col = col + (-1 if char == 'a' else 1)


            if new_col < 1 or new_col >= BOARD_WIDTH:
                self.can_move_sideways = False
                break


            if (board_state[row][new_col] != ' ' and
                (row, new_col) not in self.previous_position):
                self.can_move_sideways = False
                break

        if self.can_move_sideways:
            delta = -1 if char == 'a' else 1
            for row, col in self.previous_position:
                self.next_position.append((row, col + delta))
        else:

            for row, col in self.previous_position:
                self.next_position.append((row, col))




    def move_down(self):
        self.next_position = []
        self.can_move_down = True

        for row, col in self.previous_position:
            check_row, check_col = row + 1, col

            if check_row >= BOARD_HEIGHT:
                self.can_move_down = False
                break

            if (board_state[check_row][check_col] != ' ' and
                (check_row, check_col) not in self.previous_position):
                self.can_move_down = False
                break

        if self.can_move_down:

            for row, col in self.previous_position:
                self.next_position.append((row + 1, col))
            return True
        else:

            for row, col in self.previous_position:
                board_state[row][col] = SYMBOL
            return False

    def rotate(self):

        avg_row = sum(pos[0] for pos in self.previous_position) / len(self.previous_position)
        avg_col = sum(pos[1] for pos in self.previous_position) / len(self.previous_position)

        new_positions = []
        for row, col in self.previous_position:

            rel_row = row - avg_row
            rel_col = col - avg_col


            new_rel_row = rel_col
            new_rel_col = -rel_row


            new_row = int(avg_row + new_rel_row)
            new_col = int(avg_col + new_rel_col)

            new_positions.append((new_row, new_col))


        can_rotate = True
        for row, col in new_positions:

            if row < 0 or row >= BOARD_HEIGHT or col < 1 or col >= BOARD_WIDTH:
                can_rotate = False
                break


            if (board_state[row][col] != ' ' and
                (row, col) not in self.previous_position):
                can_rotate = False
                break


        if can_rotate:
            self.next_position = new_positions
            return True

        return False


    def draw_piece(self):
        global board_state

        for pos in self.previous_position:
            board_state[pos[0]][pos[1]] = ' '
        for pos in self.next_position:
            board_state[pos[0]][pos[1]] = SYMBOL

        self.previous_position = self.next_position.copy()










def select_piece(piece_list):
    rand_int = random.randint(1, len(piece_list)) - 1

    return Piece(piece_list[rand_int])
