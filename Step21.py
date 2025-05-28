# #Q1932
# import sys
#
# n = int(sys.stdin.readline())
# triangle = []
#
# for i in range(n) :
#     li = list(map(int, sys.stdin.readline().split()))
#     triangle.append(li)
#
# for i in range(1, n) :
#     for j in range(len(triangle[i])) :
#         if j == 0 :
#             triangle[i][j] = triangle[i][j] + triangle[i-1][j]
#         elif j == len(triangle[i]) -1 :
#             triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
#         else :
#             triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])
# print(max(triangle[n-1]))

#Q24416
import sys
sys.setrecursionlimit(10000)

def recursion(n) :
    global cnt_r
    li = [1, 1]
    for i in range(2, n) :
        li.append(li[i-1]+li[i-2])
    return li[n-1]

def dynamic(n) :
    return n-2

num = int(sys.stdin.readline())
cnt_r = recursion(num)
cnt_d = dynamic(num)
print(cnt_r, cnt_d)
