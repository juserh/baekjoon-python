# #Q2738
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
# b = [list(map(int, input().split())) for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(a[i][j]+b[i][j], end=" ")
#     print()

# #Q2566
# arr = [list(map(int, input().split())) for i in range(9)]
# m = 0
# mi = 0
# mj = 0
# for i in range(9):
#     if m <= max(arr[i]):
#         m = max(arr[i])
#         mi = i+1
#         mj = arr[i].index(m) + 1
# print(m)
# print(mi, mj)

# #Q10798
# a = [input() for i in range(5)]
# for i in range(15):
#     for j in range(5):
#         if i >= len(a[j]) : continue
#         print(a[j][i], end="")

#Q2563
# n = int(input())
# arr = list()
# for i in range(n):
#     x, y = map(int, input().split())
#     arr.append([x, y, x+10, y+10]) #x1, y1, x2, y2

