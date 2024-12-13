#Q5086
while True:
    a, b = map(int, input().split())
    if (a == 0) & (b == 0) :
        break
    if (b//a > 1) & (b%a == 0) :
        print("factor")
    elif (a//b > 1) & (a%b == 0) :
        print("multiple")
    else : # a%b != 0
        print("neither")

#Q2501
p, q = map(int, input().split())
arr = []
for i in range(1,p+1):
    if p%i == 0 :
        arr.append(i)
if q > len(arr):
    print(0)
else :
    print(arr[q-1])

#Q9506
while True:
    n = int(input())
    if n == -1 :
        break
    arr = []
    sum = 0
    for i in range(1, n) :
        if n%i == 0 :
            arr.append(i)
            sum += i
    if sum == n :
        print(f'{n} =', end=" ")
        for i in range(len(arr)) :
            print(f'{arr[i]}', end=" ")
            if i != len(arr)-1 :
                print("+", end= " ")
        print()
    else :
        print(f'{n} is NOT perfect.')

#Q1978
n = int(input())
arr = list(map(int, input().split()))
cnt = n
for a in arr :
    if a == 1 :
        cnt -= 1
        continue
    for i in range(2,a):
        if a%i == 0 : #약수
            cnt -= 1
            break
print(cnt)

#Q2581
m = int(input())
n = int(input())
arr = []
for i in range(m, n+1) :
    flag = True
    if i == 1 :
        flag = False
    for j in range(2, i) :
        if i%j == 0 :
            flag = False
            break
    if flag == True :
        arr.append(i)

if len(arr) > 0 :
    print(sum(arr))
    print(arr[0])
else :
    print(-1)

#Q11653
n = int(input())
i = 2
while n != 1 :
    if n%i != 0 :
        i += 1
    else :
        n /= i
        print(i)