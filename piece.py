import sys, tty, termios, time
from tools import set_terminal, restart_terminal, draw, clear_terminal
from board import board_state # board[row][col]
from constants import SYMBOL, BOARD_WIDTH, BOARD_HEIGHT

class Piece:
    def __init__(self, form):
        self.previous_position = form #[(a,b)(a,b)]
        self.next_position = [] #[(a,b)(a,b)]


    def move_sideways(self, char):
        self.next_position = []

        if char == 'a':
            for pos in self.previous_position:
                if pos[1] - 1 >= 0:
                    self.next_position.append((pos[0], pos[1]-1))
                else:
                    self.next_position.append((pos[0], pos[1]))

        elif char == 'd':
            for pos in self.previous_position:
                if pos[1] + 1 < BOARD_WIDTH:
                    self.next_position.append((pos[0], pos[1]+1))
                else:
                    self.next_position.append((pos[0], pos[1]))

    def move_down(self):
        self.next_position = []

        for pos in self.previous_position:
            if pos[0] + 1 < BOARD_HEIGHT:
                self.next_position.append((pos[0]+1, pos[1]))


    def draw_piece(self):
        global board_state

        for pos in self.previous_position:
            board_state[pos[0]][pos[1]] = ' '
        for pos in self.next_position:
            board_state[pos[0]][pos[1]] = SYMBOL

        self.previous_position = self.next_position.copy()


stick = Piece([(1,3),(2,3),(3,3)])
