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

    print("\033[?25h", end="", flush=True) #show cursor
    print("\033[2J", end="", flush=True) #clear terminal
    print("\033[m", end="", flush=True) #clear colors 
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def read_char():
    return sys.stdin.read(1)
