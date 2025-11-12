import curses
from curses import wrapper

import board
import display

def main(stdscr):
    border_window = curses.newwin(22, 24, 0, 0)
    active_piece_window = curses.newwin(20, 20, 1, 2)
    playing_field_window = curses.newwin(20, 20, 1, 2)
    
    display.define_color()
    board_data = board.reset_board()

    display.draw_board(border_window, board_data)

    stdscr.getch()

wrapper(main)