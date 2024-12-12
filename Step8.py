#Q2745
n, b = map(str, input().split())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
for i in range(len(n)):
    if n[i] in alpha :
        a = alpha.index(n[i]) + 10
    else :
        a = int(n[i])
    total += a*(int(b)**(len(n)-i-1))
print(total)

#Q11005
n, b = map(int, input().split())
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ntob = ""
while n > 0:
    ntob += alpha[n%b]
    n = n//b

print(ntob[::-1])

#Q2720
n = int(input())
for _ in range(n):
    change = int(input())
    q = change//25
    d = (change%25)//10
    n = (change%25%10)//5
    p = change%5
    print(q, d, n, p)

#Q2903
n = int(input())
p = 2
for i in range(n):
    p += (p-1)
print(p**2)

#Q2292
n = int(input())
cnt = 0
i = 0
while n>0:
    if i == 0:
        n -= 1
    else :
        n -= 6*i
    i += 1
    cnt += 1
print(cnt)

#Q1193
n = int(input())
cnt = 0
i = 1
while n>0 :
    n -= i
    i += 1
    cnt += 1
if cnt % 2 == 0: #짝수층
    print(f'{cnt+n}/{-n+1}')
else : #홀수층
    print(f'{-n+1}/{cnt+n}')

#Q2869
a, b, v = map(int, input().split())
day = (v-a)//(a-b) + 1
if (v-a)%(a-b) > 0:
    day += 1
print(day)