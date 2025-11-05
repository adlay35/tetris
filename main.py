import curses
from curses import wrapper

import board
import display

board = board.reset_board()

def main(stdscr):
    display.draw_board(stdscr, board)

wrapper(main)