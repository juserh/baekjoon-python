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

#Q19532
a,b,c,d,e,f = map(int,input().split())
for x in range(-999,1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            print(x, y)
            break