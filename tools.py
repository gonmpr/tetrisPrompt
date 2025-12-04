import sys, tty, termios

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)


def set_terminal():

    new_settings = old_settings.copy()

    # set non canonical mode
    new_settings[3] &= ~termios.ICANON
    new_settings[3] &= ~termios.ECHO
    new_settings[6][termios.VMIN] = 0
    new_settings[6][termios.VTIME] = 0

    termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)



    print("\033[?25l", end="", flush=True) #hidecursor
    print("\033[2J", end="", flush=True) #clear terminal


def restart_terminal():

    old_settings[3] |= termios.ECHO
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    sys.stdout.write("\033[?25h")  # show cursor
    sys.stdout.write("\033[2J")    # clear screen
    sys.stdout.write("\033[H")     # move to start
    sys.stdout.write("\033[m")     # reset colors
    sys.stdout.flush()

def read_char():
    return sys.stdin.read(1)


def draw(row, col, symbol):
    sys.stdout.write(f"\033[{row};{col}H{symbol}")
    sys.stdout.flush()
