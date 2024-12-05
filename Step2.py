#Q1330
a, b = map(int, input().split())
if (a>b): print(">")
elif (a<b): print("<")
else: print("==")

#Q9498
a = int(input())
if (a>=90 and a<=100): print("A")
elif (a>=80): print("B")
elif (a>=70): print("C")
elif (a>=60): print("D")
else: print("F")

#Q2753
a = int(input())
if ((a%4==0 and a%100!=0) or (a%400==0)): print(1)
else: print(0)

#Q14681
a = int(input())
b = int(input())
if (a>0):
    if (b>0): print(1)
    elif (b<0): print(4)
elif (a<0):
    if (b>0): print(2)
    elif (b<0): print(3)

#Q2884
h, m = map(int, input().split())
if (m>=45):
    m -= 45
else:
    if (h>=1):
        h -= 1
    else:
        h += 23
    m += 15
print(h, m)

#Q2525
h, m = map(int, input().split())
d = int(input())

h += d//60
m += d%60

if(m>=60):
    h+=1
    m-=60
if(h>=24):
    h-=24

print(h, m)

#Q2480
a, b, c = map(int, input().split())
if (a==b and b==c):
    total = 10000 + a*1000
else:
    if (a==b or a==c):
        total = 1000 + a*100
    elif (b==c):
        total = 1000 + b*100
    else:
        total = max(a,b,c)*100
print(total)