def reset_board():
    """게임 보드를 초기화하는 함수.

    가로 10칸, 세로 20칸에 벽을 1칸씩

    Returns:
        list: 초기화된 게임 보드 값이 담긴 2차원 리스트
    """
    board = []

    board.append([8 for x in range(22)])    #시작부분 벽 라인
    for i in range(20):
        board.append([8,0,0,0,0,0,0,0,0,0,0,8]) #중간 20 라인
    board.append([8 for x in range(22)])    #끝부분 벽 라인

    return board