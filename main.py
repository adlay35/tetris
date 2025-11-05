import curses
from curses import wrapper

import board
import display

board = board.reset_board()

def main(stdscr):
    # 색상지정
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    
    display.draw_board(stdscr, board)

wrapper(main)