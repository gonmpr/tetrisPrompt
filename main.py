import sys, tty, termios, time, random
from tools import set_terminal, read_char, restart_terminal, draw, clear_terminal, draw_text
from board import board_state, make_empty_board, check_and_clear_lines, check_game_over
from constants import SYMBOL
from piece import Piece, select_piece

forms = [
            [(1, 10),(2,10),(3,10)],
            [(1, 10),(2,10),(1,11),(2,11)],
            [(1,9),(1, 10),(2,10),(3,10)],
            [(2,9),(2,10),(2,11),(1,10)]
        ]



def main():
    last_time = time.time()
    normal_delay = 0.5
    current_delay = normal_delay

    score = 0
    piece = select_piece(forms)

    set_terminal()
    make_empty_board()




    while True:
        current_time = time.time()
        char = read_char()

        if char == 'q':
            break
        if char == 's':
            current_delay = 0
        else:
            current_delay = normal_delay

        if char == 'w':
            if piece.rotate():
                piece.draw_piece()
                draw(score)

        if char in ['a', 'd'] and piece.can_move_down:

            piece.move_sideways(char)
            piece.draw_piece()
            draw(score)


        if current_time - last_time >= current_delay:
            if piece.move_down():
                piece.draw_piece()
            else:
                lines = check_and_clear_lines()
                score += lines
                piece = select_piece(forms)

                if check_game_over():
                    break
            draw(score)



            last_time = current_time




        time.sleep(0.01)

    restart_terminal()
    print('GAME OVER!')
    print(f'Your final score was: {score}')







if __name__ == "__main__":
    main()
