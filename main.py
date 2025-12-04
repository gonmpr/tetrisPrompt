import sys, tty, termios, time
from tools import set_terminal, read_char, restart_terminal, draw

def main():

    i=0
    set_terminal()

    while True:
        char = read_char()

        if char == 'q':
            break

        draw(5+i,10,'#')
        draw(6+i,10,'#')

        time.sleep(3)

        i += 1
        set_terminal()


    restart_terminal()

if __name__ == "__main__":
    main()
