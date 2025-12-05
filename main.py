import sys, tty, termios, time
from tools import set_terminal, read_char, restart_terminal, draw, clear_terminal
from board import board_state, make_empty_board
from constants import SYMBOL
from piece import stick

def main():
    last_time = time.time()
    frame_delay = 0.5

    set_terminal() # set the terminal to game mode
    make_empty_board() # creates an empty board




    while True:
        current_time = time.time()
        char = read_char() # read user input

        if char == 'q':
            break

        if char in ['a', 'd']:
            stick.move_sideways(char)
            stick.draw_piece()
            draw()


        if current_time - last_time >= frame_delay: #if the time passed, it will render 
            stick.move_sideways(char)
            stick.move_down()
            stick.draw_piece()
            draw()



            last_time = current_time





        time.sleep(0.01) #just because

    restart_terminal() #puts the terminal in normal mode again

if __name__ == "__main__":
    main()
