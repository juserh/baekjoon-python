# #Q2798
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)
#
# total_m = 0
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1, n):
#             total = arr[i] + arr[j] + arr[k]
#             if (total<=m) and (total>total_m):
#                 total_m = total
# print(total_m)

# #Q2231
# n = int(input())
#
# for i in range(1,n+1):
#     num = sum((map(int, str(i))))
#     num_sum = i+num
#     if num_sum == n:
#         print(i)
#         break
#     if i ==n :
#         print(0)

# #Q19532
# a,b,c,d,e,f = map(int,input().split())
# for x in range(-999,1000):
#     for y in range(-999, 1000):
#         if (a*x + b*y == c) and (d*x + e*y == f):
#             print(x, y)
#             break

#Q1018
n, m = map(int, input().split())
board = []
swb = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB', 'BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
sww = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW' ]
for i in range(n):
    l = input()
    board.append(l)

minimum = 64
for i in range(0, m-7) : #가로
    for j in range(0, n-7) : #세로
        b8 = board[j:j+8]
        b8 = list(map(lambda ll : ll[i:i+8], b8))
        cb = 0
        cw = 0
        for line in range(8) :
            cb += sum(b8[line][ch1] != swb[line][ch1] for ch1 in range(8))
            cw += sum(b8[line][ch2] != sww[line][ch2] for ch2 in range(8))
        if minimum > min(cb, cw) :
            minimum = min(cb,cw)
print(minimum)