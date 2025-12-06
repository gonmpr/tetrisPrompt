import termios, sys
from constants import BOARD_HEIGHT, BOARD_WIDTH


board_state = []

def make_empty_board():
    global board_state
    for row in range(BOARD_HEIGHT):
        board_state.append([])
        for col in range(BOARD_WIDTH):
            board_state[-1].append(' ')



def check_and_clear_lines():
    lines_cleared = 0
    row = BOARD_HEIGHT - 1

    while row >= 0:

        is_full = True
        for col in range(1, BOARD_WIDTH):
            if board_state[row][col] == ' ':
                is_full = False
                break

        if is_full:

            for col in range(BOARD_WIDTH):
                board_state[row][col] = ' '


            for r in range(row, 0, -1):
                board_state[r] = board_state[r-1].copy()


            board_state[0] = [' ' for _ in range(BOARD_WIDTH)]

            lines_cleared += 1
        else:
            row -= 1

    return lines_cleared





def check_game_over():

    for col in range(1, BOARD_WIDTH):
        if board_state[0][col] != ' ':
            return True

    spawn_positions = [
        (1, 9), (1, 10), (1, 11),
        (2, 9), (2, 10), (2, 11),
        (3, 9), (3, 10)
    ]

    for row, col in spawn_positions:
        if board_state[row][col] != ' ':
            return True

    return False
