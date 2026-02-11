# GPT
from collections import deque, Counter

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs_extract(board, target):
    n = len(board)
    visited = [[False]*n for _ in range(n)]
    shapes = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == target:
                q = deque([(i, j)])
                visited[i][j] = True
                cells = [(i, j)]

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cells.append((nx, ny))

                shapes.append(cells)
    return shapes

def normalize(cells):
    xs = [x for x, y in cells]
    ys = [y for x, y in cells]
    minx, miny = min(xs), min(ys)
    norm = sorted((x - minx, y - miny) for x, y in cells)
    return tuple(norm)

def rotate90(cells):
    # cells: list/tuple of (x,y) in normalized-ish coordinates
    # (x,y) -> (y, -x)
    rotated = [(y, -x) for x, y in cells]
    return normalize(rotated)

def canonical(cells):
    base = normalize(cells)
    forms = [base]
    cur = base
    for _ in range(3):
        cur = rotate90(cur)
        forms.append(cur)
    return min(forms)  # 대표 형태(회전 불변 키)

def solution(game_board, table):
    # 1) table에서 조각들(1) 추출
    pieces = bfs_extract(table, 1)
    piece_counter = Counter()
    piece_size = {}

    for p in pieces:
        key = canonical(p)
        piece_counter[key] += 1
        piece_size[key] = len(p)  # 같은 key는 크기 동일

    # 2) game_board에서 구멍들(0) 추출
    holes = bfs_extract(game_board, 0)

    ans = 0
    for h in holes:
        key = canonical(h)
        if piece_counter[key] > 0:
            piece_counter[key] -= 1
            ans += len(h)
    return ans


# Programmers
# from collections import Counter
# from dataclasses import dataclass
# from itertools import product
#
# @dataclass(frozen=True)
# class Pos:
#     x: int
#     y: int
#
#     def neighbors(self):
#         return [
#             Pos(self.x, self.y - 1),
#             Pos(self.x + 1, self.y),
#             Pos(self.x, self.y + 1),
#             Pos(self.x - 1, self.y),
#         ]
#
#
# def make_tile_from_positions(positions):
#     """Smallest possible representation with rotation"""
#
#     def rotate90(tile):
#         return tuple(
#             tuple(tile[i][j] for i in range(len(tile)))
#             for j in reversed(range(len(tile[0])))
#         )
#
#     positions = set(positions)
#
#     xs = [pos.x for pos in positions]
#     min_x = min(xs)
#     max_x = max(xs)
#
#     ys = [pos.y for pos in positions]
#     min_y = min(ys)
#     max_y = max(ys)
#
#     tile_representations = [
#         tuple(
#             tuple(Pos(i, j) in positions for j in range(min_y, max_y + 1))
#             for i in range(min_x, max_x + 1)
#         )
#     ]
#
#     for __ in range(3):
#         tile_representations.append(rotate90(tile_representations[-1]))
#
#     return min(tile_representations)
#
#
# def get_tile_size(tile):
#     return sum(sum(row) for row in tile)
#
#
# def parse_tiles(board, tile_value=1):
#     n = len(board)
#
#     # Add sentinel boundaries
#     sentinel = 1 - tile_value
#
#     board = [
#         [sentinel] * (n + 2),
#         *([sentinel] + row + [sentinel] for row in board),
#         [sentinel] * (n + 2),
#     ]
#
#     # Detect tiles
#     tile_positions = []
#     for i, j in product(range(1, n + 1), range(1, n + 1)):
#         if board[i][j] == tile_value:
#             stack = [Pos(i, j)]
#             squares = []
#             while stack:
#                 curr = stack.pop()
#                 board[curr.x][curr.y] = sentinel
#                 squares.append(curr)
#                 for neighbor in curr.neighbors():
#                     if board[neighbor.x][neighbor.y] == tile_value:
#                         stack.append(neighbor)
#             tile_positions.append(squares)
#
#     # Make tiles
#     tiles = [make_tile_from_positions(p) for p in tile_positions]
#
#     return tiles
#
#
# def solution(game_board, table):
#     tiles = parse_tiles(table, 1)
#     empty_spaces = parse_tiles(game_board, 0)
#
#     tile_counter = Counter(tiles)
#     empty_space_counter = Counter(empty_spaces)
#
#     used_tiles = tile_counter & empty_space_counter
#
#     return sum(get_tile_size(tile) * occ for tile, occ in used_tiles.items())