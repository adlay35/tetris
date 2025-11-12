import curses
from curses import wrapper

import board, display, tetromino

def main(stdscr):
    curses.curs_set(0)

    # TODO: 매직넘버 수정하기 (board.py의 상수 이쪽으로 옮기기!)
    border_window = curses.newwin(23, 24, 0, 0)
    active_piece_window = curses.newwin(20, 20, 1, 2)
    playing_field_window = curses.newwin(20, 20, 1, 2)
    
    display.define_color()
    board_data = board.reset_board()

    display.draw_board(border_window, board_data)

    tetromino_table = tetromino.reset_tetromino_table()

    game_over = False
    while (game_over == False):
        # playing_field_window.refresh()

        new_piece, tetromino_table = tetromino.spawn_tetromino(tetromino_table)
        display.draw_piece(active_piece_window, new_piece)

        stdscr.getch()


wrapper(main)