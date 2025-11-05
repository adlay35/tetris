import curses

# 각 역할 맞게 색을 칠해주는 함수
# 빈공간은 0,벽은1, 블럭은 각각의 색에 맞게?
def color_block(stdscr, y, x, color_id):
    if color_id == 0:
        stdscr.addstr(y, 2*x, "  ")
    else:
        stdscr.addstr(y, 2*x, "  ", curses.color_pair(color_id))

def draw_board(stdscr, board):
    stdscr.clear()

    for i in range(22):
        for j in range(12):
            color_block(stdscr, i, j, board[i][j])
    
    stdscr.refresh()
    stdscr.getch()