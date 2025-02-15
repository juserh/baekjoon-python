#Q2750
n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(input()))
#(1)
arr.sort()
for a in arr :
    print(a)

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

#Q2587
arr = []
for _ in range(5) :
    arr.append(int(input()))

print(int(sum(arr)/5))
print(sorted(arr)[2])

#Q25305
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(sorted(arr)[-k])

#Q2751
import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
for a in sorted(arr) :
    print(a)

#Q10989
import sys
n = int(input())
arr = [0 for _ in range(10000)]
for _ in range(n) :
    arr[int(sys.stdin.readline())-1] += 1
for i in range(len(arr)) :
    if arr[i] != 0 :
        for _ in range(arr[i]) :
            print(i+1)

#Q1427
n=list(map(int,input()))
#n.sort(reverse=True)
for a in sorted(n, reverse=True) :
    print(a,end="")

#Q11650
n = int(input())
arr = []
for _ in range(n) :
    x, y = map(int, input().split())
    arr.append([x,y])
for a in sorted(arr) : #or arr.sort()
    print(a[0],a[1])

#Q11651
n = int(input())
arr = []
for _ in range(n) :
    x, y = map(int, input().split())
    arr.append([x,y])
arr.sort(key = lambda x : (x[1], x[0]))
for a in arr :
    print(a[0],a[1])

#Q1181
n = int(input())
arr = []
for _ in range(n) :
    arr.append(input()) #arr.append(sys.stdin.readline().strip())
arr = list(set(arr))
arr.sort(key = lambda x : (len(x), x))
for w in arr :
    print(w)

#Q10814
n = int(input())
arr = []
for i in range(n):
    age, name = map(str, input().split())
    arr.append([int(age), name])
arr.sort(key= lambda x: x[0])
for a in arr :
    print(a[0], a[1])

#Q18870
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
s_arr = sorted(list(set(arr)))
dic = {s_arr[i] : i for i in range(len(s_arr))}
for a in arr :
    print(dic[a], end=" ")
