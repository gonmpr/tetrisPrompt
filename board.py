import termios, sys
from constants import BOARD_HEIGHT, BOARD_WIDTH


board_state = []

def make_empty_board():
    global board_state
    for row in range(BOARD_HEIGHT):
        board_state.append([])
        for col in range(BOARD_WIDTH):
            board_state[-1].append(' ')


