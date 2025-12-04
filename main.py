import sys, tty, termios, time
from tools import set_terminal, read_char, restart_terminal, draw, clear_terminal

def main():
    last_time = time.time()
    frame_delay = 0.5


    i=0
    set_terminal()

    while True:
        current_time = time.time()


        # read input
        char = read_char()
        if char == 'q':
            break




        if current_time - last_time >= frame_delay: #logic/render 


            clear_terminal()
            draw(5+i,10,'#')
            draw(6+i,10,'#')


            last_time = current_time
            i += 1





        time.sleep(0.01)

    restart_terminal()

if __name__ == "__main__":
    main()
