import random

tertomino = {
'i': [[0,0,0,0],
      [1,1,1,1],
      [0,0,0,0],
      [0,0,0,0]],

'j': [[2,0,0],
      [2,2,2],
      [0,0,0]],

'l': [[0,0,3],
      [3,3,3],
      [0,0,0]],

'o': [[4,4],
      [4,4]],

's': [[0,5,5],
      [5,5,0],
      [0,0,0]],

't': [[0,6,0],
      [6,6,6],
      [0,0,0]],

'z': [[7,7,0],
      [0,7,7],
      [0,0,0]]
}

TETROMINO_KEY_NAME = {
    1: 'i',
    2: 'j',
    3: 'l',
    4: 'o',
    5: 's',
    6: 't',
    7: 'z'
}

def reset_tetromino_table():
    """랜덤한 블럭의 순서가 담긴 리스트를 반환하는 함수.

    7가지 블럭이 랜덤하게 생성되는 '7-bag' 시스템을 구현
    완전히 무작위성이 아닌, 한 사이클에 반드시 모든 종류의 블럭이 한번씩 나와야하는 구조

    Returns:
        list: 다음 사이클에서 출력해야할 블럭의 순서가 담긴 리스트
    """
    tetromino_table = [x for x in range(1,8)]
    random.shuffle(tetromino_table)

    return tetromino_table


def spawn_tetromino(tetromino_table = None):
    """다음에 생성할 테트로미노를 결정한뒤 데이터를 반환하는 함수.

    다음 생성될 테트로미노의 데이터를 뽑고, 해당 ID를 테이블에서 제거 (pop).
    테이블이 비어있다면 reset_tetromino_table()을 호출하여 테이블을 재설정.

    Args:
        tetromino_table(list, optional): 현재 남아있는 블록 ID(1~7) 리스트.
                                         함수 호출 시 명시적으로 전달되지 않으면, (None인 경우)
                                         함수 내부에서 빈 리스트([])로 처리됨
    Returns:
        tuples: 다음 두 요소를 포함하는 튜플:
            1. dict: 새롭게 생성된 블록의 상태 정보 (id, 모양, 위치 등)
            2. list: 블록 id가 하나 제거된 업데이트된 테이블 리스트
    """

    if tetromino_table is None:
        tetromino_table = []
    
    if len(tetromino_table) == 0:
        tetromino_table = reset_tetromino_table()  

    n = tetromino_table.pop()

    # 테트로미노 딕셔너리 값 인출
    key_name = TETROMINO_KEY_NAME[n]
    tetromino_data = tertomino[key_name]

    initial_x = 4 * 2    # 보드의 가로축 중앙에서 시작
    initial_y = 1        # 제일 위에서 시작

    new_piece = {
        'block_id': n,
        'tetromino_data': tetromino_data,
        'current_x': initial_x,
        'current_y': initial_y
    }

    return new_piece, tetromino_table