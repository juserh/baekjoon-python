#Q10807
n = int(input())
arr = list(map(int, input().split()))
a = int(input())
print(arr.count(a))

#Q10871
n, x = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    if (arr[i]<x):
        print(arr[i], end=" ")

#Q10818
n = int(input())
arr = list(map(int, input().split()))
print(min(arr), max(arr))

#Q2562
arr = list()
for i in range(9):
    arr.append(int(input()))
print(max(arr), arr.index(max(arr))+1)

#Q10810
n, m = map(int, input().split())
arr = [0 for i in range(n)]
for p in range(m):
    i, j, k = map(int, input().split())
    for q in range(i-1, j):
        arr[q] = k
for q in range(n):           #print(*arr) : 반복문 없이 한번에 출력 가능
    print(arr[q], end=" ")

#Q10813
n, m = map(int, input().split())
arr = [(i+1) for i in range(n)]
for p in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
print(*arr)

#Q5597
arr = [0 for i in range(30)] #1-30번 -> index: 0-29
for i in range(28):
    n = int(input())
    arr[n-1] = 1
arr_x = list(filter(lambda x: arr[x-1] == 0, range(1,31)))
print(*arr_x)

#Q3052
arr = [0 for i in range(42)]
for i in range(10):
    n = int(input())
    arr[n%42] = 1
print(arr.count(1))

#Q10811
n, m = map(int, input().split())
arr = [(i+1) for i in range(n)] #1-n번 바구니
for p in range(m):
    i, j = map(int, input().split())
    i -= 1
    arr[i:j] = list(reversed(arr[i:j]))
print(*arr)

#Q1546
n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
arr = [arr[i]/m*100 for i in range(n)]
print(sum(arr)/n)