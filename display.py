import curses
from curses import wrapper

def draw_block(stdscr):
    stdscr.clear()
    #color pieces
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.addstr(1,0,"  ", curses.color_pair(1))

    stdscr.getch()

wrapper(draw_block)