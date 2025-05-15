# #Q15649
# import sys
#
# def backtracking(li, num) :
#     global m
#     if len(li) == m :
#         print(' '.join(map(str, li)))
#
#     for i in range(1, num+1) :
#         if i not in li :
#             li.append(i)
#             backtracking(li, num)
#             li.pop()
#
#
# n, m = map(int, sys.stdin.readline().split())
# backtracking([], n)

# #Q15650
# import sys
#
# def backtracking(li, num) :
#     global m
#     global visited
#     if len(li) == m :
#         print(' '.join(map(str, li)))
#
#     for i in range(1, num+1) :
#         if visited[i-1] == 0 :
#             if len(li) == 0 or li[-1] < i :
#                 li.append(i)
#                 visited[i-1] = 1
#                 backtracking(li, num)
#                 li.pop()
#                 visited[i-1] = 0
#
#
# n, m = map(int, sys.stdin.readline().split())
# visited = [0] * n
# backtracking([], n)

# #Q15651
# import sys
#
# def backtracking(li, num) :
#     global m
#     if len(li) == m :
#         print(' '.join(map(str, li)))
#         return
#
#     for i in range(1, num+1) :
#         li.append(i)
#         backtracking(li, num)
#         li.pop()
#
# n, m = map(int, sys.stdin.readline().split())
# backtracking([], n)

# #Q15652
# import sys
#
# def backtracking(li, num) :
#     global m
#     if len(li) == m :
#         print(' '.join(map(str, li)))
#         return
#
#     start = 1
#     if len(li) > 0 :
#         start = li[-1]
#
#     for i in range(start, num+1) :
#         li.append(i)
#         backtracking(li, num)
#         li.pop()
#
# n, m = map(int, sys.stdin.readline().split())
# backtracking([], n)

#Q9663
import sys

n = int(sys.stdin.readline())
board = [-1]*n # index : 각 row, value : 해당 row에서의 퀸 위치
cnt = 0

def check(row) :
    for r in range(row):
        if board[r] == board[row] or row - r == abs(board[row] - board[r]):
            return False
    return True

def place_queen(row, size) : #체스 보드판, 놓아야할 퀸 개수
    global cnt

    if row == size :
        cnt += 1

    else :
        for col in range(size) :
            board[row] = col
            if check(row) :
                place_queen(row+1, size)

place_queen(0, n)
print(cnt)