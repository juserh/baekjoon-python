#Q25083
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")
print("      |")
print("      |")

#Q3003
chess = [1, 1, 2, 2, 2, 8]
d = list(map(int, input().split()))
for i in range(len(chess)):
    print(chess[i]-d[i], end=" ")

#Q2444
n = int(input()) #5
for i in range(2*n-1): #0 1 2 3 4 / 5 6 7 8
    star = ""
    if i < n:
        star += " "*(n-i-1) #4 3 2 1 0
        star += "*"*(2*i+1) #1 3 5 7 9
    else:
        star += " "*(i-n+1) #1 2 3 4
        star += "*"*(4*n-2*i-3) #7 5 3 1
    print(star)

#Q10988
s = input()
if s == s[::-1] :
    print(1)
else :
    print(0)

#Q1157
s = input().upper()
ss = list(set(s))
c = [s.count(ch) for ch in ss]
if c.count(max(c)) > 1 :
    print("?")
else :
    print(ss[c.index(max(c))])

#Q2941
s = input()
alphabet = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}
c = 0
i =0
while(1):
    if i >= len(s): break
    if s[i:i+3] in alphabet:
        c +=1
        i +=3
    elif s[i:i+2] in alphabet:
        c +=1
        i +=2
    else :
        c +=1
        i +=1
print(c)

#Q1316
n = int(input())
c = 0
for i in range(n): #aaabaa
    w = input()
    flag = True
    for j in range(len(w)):
        for k in range(j+1, len(w)):
            if (w[j] == w[k]) & (w[k] != w[k-1]):
                flag = False
    if flag == True:
         c += 1
print(c)

#Q25206
total = 0
n = 0
for i in range(20):
    subject, etc, grade = map(str, input().split())
    etc = float(etc)
    if grade == "A+" : grade = 4.5
    elif grade == "A0" : grade = 4.0
    elif grade == "B+" : grade = 3.5
    elif grade == "B0" : grade = 3.0
    elif grade == "C+" : grade = 2.5
    elif grade == "C0" : grade = 2.0
    elif grade == "D+" : grade = 1.5
    elif grade == "D0" : grade = 1.0
    elif grade == "F" : grade = 0.0
    else : #P
        continue
    total += etc*grade
    n += etc
print(total/n)

