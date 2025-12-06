import sys, tty, termios
from board import board_state
from constants import SYMBOL, BOARD_HEIGHT, BOARD_WIDTH

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)


# puts the terminal in game mode
def set_terminal():

    new_settings = old_settings.copy()

    # set non canonical mode
    new_settings[3] &= ~termios.ICANON
    new_settings[3] &= ~termios.ECHO
    new_settings[6][termios.VMIN] = 0
    new_settings[6][termios.VTIME] = 0

    termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)

    print("\033[?25l", end="", flush=True) #hidecursor

def draw_borders():
    for i in range(BOARD_WIDTH):
        sys.stdout.write(f"\033[{1};{i+1}H{'-'}")
        sys.stdout.write(f"\033[{BOARD_HEIGHT};{i+1}H{'-'}")

    for i in range(BOARD_HEIGHT):
        sys.stdout.write(f"\033[{i+1};{1}H{'|'}")
        sys.stdout.write(f"\033[{i+1};{BOARD_WIDTH + 1}H{'|'}")



# for clearing the last render
def clear_terminal():
    print("\033[2J\033[3J\033[H", end="", flush=True)
    draw_borders()


# restore the terminal
def restart_terminal():

    old_settings[3] |= termios.ECHO
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    sys.stdout.write("\033[?25h")  # show cursor
    sys.stdout.write("\033[2J")    # clear screen
    sys.stdout.write("\033[H")     # move to start
    sys.stdout.write("\033[m")     # reset colors
    sys.stdout.flush()




# read user input
def read_char():
    return sys.stdin.read(1)





# draw a symbol in the given position
def draw():
    clear_terminal()


    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):

            if board_state[row][col] != ' ':

                sys.stdout.write(f"\033[{row+1};{col+1}H{SYMBOL}")
                sys.stdout.flush()



