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

#Q15652
import sys

def backtracking(li, num) :
    global m
    if len(li) == m :
        print(' '.join(map(str, li)))
        return

    start = 1
    if len(li) > 0 :
        start = li[-1]

    for i in range(start, num+1) :
        li.append(i)
        backtracking(li, num)
        li.pop()

n, m = map(int, sys.stdin.readline().split())
backtracking([], n)