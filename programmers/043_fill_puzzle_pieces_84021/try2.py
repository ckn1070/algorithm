# NOT Solved
# 빈 칸 떼어내고, 퍼즐 떼어내서 비교하면 될 것 같은데
# 떼어내는게 1차 관문, 그걸 원점이동 시키는게 2차 관문일 것 같은데
# 아 도형 회전이 3차 관문..
# 1번 방법은 아닌것같아. 전부 떼어내면 그것만 해도 코드가 산더미
# Try 1
def solution(game_board, table):
    empties = []
    puzzles = []
    n = len(game_board)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for j in range(len(game_board)):
        for i in range(len(game_board[0])):
            tmp = []
            if game_board[j][i] == 1:
                continue
            game_board[j][i] = 0
            tmp.append((i, j))
            for dx, dy in dirs:
                nx = i + dx
                ny = j + dy
                if 0<=nx<n and 0<=ny<n and game_board[ny][nx] == 0:
                    tmp.append((nx, ny))
                    game_board[ny][nx] = 1
            empties.append(tmp)
    print(empties)

    answer = -1
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]])