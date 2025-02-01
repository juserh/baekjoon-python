# #Q2750
# n = int(input())
# arr = []
# for _ in range(n) :
#     arr.append(int(input()))
# #(1)
# # arr.sort()
# # for a in arr :
# #     print(a)
#
# #(2) -버블정렬
# for i in range(n-1,-1,-1) :
#     for j in range(0, i) :
#         if arr[j] > arr[j+1] :
#             tmp = arr[j+1]
#             arr[j+1] = arr[j]
#             arr[j] = tmp
#
# for a in arr :
#     print(a)

# #Q2587
# arr = []
# for _ in range(5) :
#     arr.append(int(input()))
#
# print(int(sum(arr)/5))
# print(sorted(arr)[2])

#Q25305
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(sorted(arr)[-k])
