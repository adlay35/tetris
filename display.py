import curses

def define_color():
    """curses 환경에서 출력에 사용할 색상을 정의하고, 초기화하는 함수.
    
    - 색상 1~7: 테트로미노 색상
    - 색상 8: 벽 색상
    - 참고: 빈 공간(0)은 별도의 색상 정의 없이 기본 배경색을 사용
    """
    curses.initscr()
    curses.start_color()

    curses.init_color(1, 0, 999, 999)   # Cyan
    curses.init_color(2, 0, 000, 999)   # Blue
    curses.init_color(3, 999, 666, 0)   # Orange
    curses.init_color(4, 999, 999, 000) # Yellow
    curses.init_color(5, 0, 999, 0)     # Green
    curses.init_color(6, 600, 0, 999)   # Purple
    curses.init_color(7, 999, 0, 0)     # Red
    curses.init_color(8, 999, 999, 999) # White

    curses.init_pair(1, 1, 1)   # 1번에 Cyan을 할당 
    curses.init_pair(2, 2, 2)   # .
    curses.init_pair(3, 3, 3)   # .
    curses.init_pair(4, 4, 4)   # .
    curses.init_pair(5, 5, 5)   # .
    curses.init_pair(6, 6, 6)   # .
    curses.init_pair(7, 7, 7)   # .
    curses.init_pair(8, 8, 8)   # 8번에 White을 할당


def color_block(stdscr, y, x, block_id):
    """입력받은 좌표의 블럭 색을 출력해주는 함수.

    터미널 글자 간격 때문에 가로칸은 2칸이 1칸이 되어야 정사각형이 됨

    Args:
        stdscr (object): 출력에 사용할 curses의 윈도우 객체
        y (int): 출력할 지점의 y좌표 (행)
        x (int): 출력할 지점의 x좌표 (열, 내부적으로 2*x로 변환됨)
        block_id (int): 출력할 지점의 색상 id (0: 빈공간, 1~8: 정의된 색상)
    """
    if block_id == 0:
        stdscr.addstr(y, 2*x, "  ")
    else:
        stdscr.addstr(y, 2*x, "  ", curses.color_pair(block_id))


def draw_board(stdscr, board):
    stdscr.clear()

    for i in range(22):
        for j in range(12):
            color_block(stdscr, i, j, board[i][j])
    
    stdscr.refresh()
    stdscr.getch()