# import curses

board = []

board.append([1 for x in range(22)])    #시작부분 벽 라인
for i in range(20):
    board.append([1,0,0,0,0,0,0,0,0,0,0,1]) #중간 20 라인
board.append([1 for x in range(22)])    #끝부분 벽 라인

print(board)