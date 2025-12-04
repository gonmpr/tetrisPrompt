import sys, tty, termios
from tools import set_terminal, read_char, restart_terminal

def main():


    set_terminal()

    while True:
        char = read_char()

        if char == 'q':
            break

    restart_terminal()

if __name__ == "__main__":
    main()
