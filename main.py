import curses
from curses import wrapper

import board
import display

board = board.reset_board()
display.define_color()

def main(stdscr):
    display.draw_board(stdscr, board)

wrapper(main)