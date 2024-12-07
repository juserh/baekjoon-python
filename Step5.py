#Q27866
s = input()
i = int(input())
print(s[i-1])

#Q2743
s = input()
print(len(s))

#Q9086
n = int(input())
for i in range(n):
    s = input()
    print(s[0]+s[-1])

#Q11654
s = ord(input()) #ord(문자): chr->ascii / chr(아스키코드 숫자): ascii->chr
print(s)

#Q11720
n = int(input())
arr = input()
sum = 0
for i in range(n):
    sum += int(arr[i])
print(sum)

#Q10809
s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for a in alphabet:
    print(s.find(a), end=" ")

#Q2675
n = int(input())
for i in range(n):
    r, s = map(str, input().split())
    se=""
    for j in range(len(s)):
        se += s[j]*int(r)
    print(se)

#Q1152
s = input().split()
print(len(s))

#Q2908
a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]
print(max(a, b))

#Q5622
s = input()
sum = 0
for c in s:
    if (c in "ABC") : sum+=3
    elif (c in "DEF") : sum+=4
    elif (c in "GHI") : sum+=5
    elif (c in "JKL") : sum+=6
    elif (c in "MNO") : sum+=7
    elif (c in "PQRS") : sum+=8
    elif (c in "TUV") : sum+=9
    else : sum+=10
print(sum)

#Q11718
#1
import sys
s = sys.stdin.readlines()
for i in s:
    print(i.rstrip())

#2
while True:
    try:
        print(input())
    except EOFError:
        break
