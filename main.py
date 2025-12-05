import sys, tty, termios, time
from tools import set_terminal, read_char, restart_terminal, draw, clear_terminal
from board import board_state, make_empty_board
from constants import SYMBOL

def main():
    last_time = time.time()
    frame_delay = 0.5

    set_terminal() # set the terminal to game mode
    make_empty_board() # creates an empty board

    board_state [0][2] = SYMBOL
    board_state [1][2] = SYMBOL







    while True:
        current_time = time.time()
        char = read_char() # read user input

        if char == 'q':
            break




        if current_time - last_time >= frame_delay: #if the time passed, it will render 
            draw()



            last_time = current_time





        time.sleep(0.01) #just because

    restart_terminal() #puts the terminal in normal mode again

if __name__ == "__main__":
    main()
