WALL_CHELL = 8
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
TOTAL_COLS = BOARD_WIDTH + 2
TOTAL_ROWS = BOARD_HEIGHT + 2

def reset_board():
    """게임 보드를 초기화하는 함수.

    가로 10칸, 세로 20칸에 벽을 1칸씩

    Returns:
        list: 초기화된 게임 보드 값이 담긴 2차원 리스트
    """
    top_wall = [WALL_CHELL] * TOTAL_COLS
    middle_wall = [WALL_CHELL] + ([0] * BOARD_WIDTH) + [WALL_CHELL]

    board = [top_wall] + ([middle_wall] * BOARD_HEIGHT) + [top_wall]

    return board

print(reset_board())