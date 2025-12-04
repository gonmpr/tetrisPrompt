import sys, tty, termios, time
from tools import set_terminal, read_char, restart_terminal, draw, clear_terminal


class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parts = []
        self.canMove = True


    def move(self):
        char = read_char()

        if char == 'a':
            #move all left
        if char == 'd':
            #move all right 

    def rotate(self):
        char = read_char()

        if char == 'r':
            #rotates clockwise

    def collides_with(self, other)
            #if bottom part collides with a block, it stop
            #if it touch the borders, can no move to that side
