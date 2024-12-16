#Q27323
a = int(input())
b = int(input())
print(a*b)

#Q1085
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

#Q3009
arrx = []
arry = []
for _ in range(3):
    x, y = map(int, input().split())
    arrx.append(x)
    arry.append(y)

for i in range(3) :
    if arrx.count(arrx[i]) == 1 :
        xe = arrx[i]
    if arry.count(arry[i]) == 1 :
        ye = arry[i]
print(xe, ye)

#Q15894
n = int(input())
if n == 1:
    total = 4
else :
    total = n + 3*n
print(total)

#Q9063
n = int(input())
arrx = []
arry = []
for _ in range(n) :
    x, y = map(int, input().split())
    arrx.append(x)
    arry.append(y)
w = max(arrx) - min(arrx)
h = max(arry) - min(arry)
print(w*h)

#Q10101
a = [int(input()) for _ in range(3)]
if sum(a) != 180 :
    print("Error")
else :
    if (a[0] == a[1]) and (a[1] == a[2]) :
        print("Equilateral")
    elif (a[0] == a[1]) or (a[1] == a[2]) or (a[0] == a[2]) :
        print("Isosceles")
    else :
        print("Scalene")

#Q5073
while True :
    arr = list(map(int, input().split()))
    if (arr[0]==0) and (arr[1]==0) and (arr[2]==0) :
        break
    else :
        if max(arr) >= sum(arr) - max(arr) :
            print("Invalid")
        elif (arr[0]==arr[1]) and (arr[1]==arr[2]) :
            print("Equilateral")
        elif (arr[0]==arr[1]) or (arr[1]==arr[2]) or (arr[0]==arr[2]) :
            print("Isosceles")
        else :
            print("Scalene")

#Q14215
arr = list(map(int, input().split()))
m = max(arr)
if m >= sum(arr)-m :
    arr[arr.index(m)] = sum(arr)-m-1
print(sum(arr))
