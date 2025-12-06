import sys, tty, termios, time, random
from tools import set_terminal, read_char, restart_terminal, draw, clear_terminal
from board import board_state, make_empty_board
from constants import SYMBOL
from piece import Piece, select_piece

forms = [
            [(1, 10),(2,10),(3,10)], # palo
            [(1, 10),(2,10),(1,11),(2,11)], #cubo
            [(1,9),(1, 10),(2,10),(3,10)], # ele
            [(2,9),(2,10),(2,11),(1,10)] # interseccion?
        ]




def main():
    last_time = time.time()
    frame_delay = 0.5

    piece = select_piece(forms)

    set_terminal() # set the terminal to game mode
    make_empty_board() # creates an empty board




    while True:
        current_time = time.time()
        char = read_char() # read user input

        if char == 'q':
            break
        if char in ['a', 'd'] and piece.can_move_down:

            piece.move_sideways(char)
            piece.draw_piece()
            draw()


        if current_time - last_time >= frame_delay: #if the time passed, it will render 
            if piece.move_down():
                piece.draw_piece()
            else:
                piece = select_piece(forms)
            draw()



            last_time = current_time





        time.sleep(0.01) #just because

    restart_terminal() #puts the terminal in normal mode again

if __name__ == "__main__":
    main()
